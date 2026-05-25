"""
DeepSeek-v4 API 调用模块 — OpenAI-compatible chat completions 接口。

提供 call_deepseek_json() 用于严格信息抽取。
任何 chunk 调用失败不中断整个任务，写入 unresolved_items.yaml。
日志中绝不打印 API key。
"""

import json
import logging
import os
import re
import sys
from pathlib import Path

import yaml
from dotenv import load_dotenv
from openai import OpenAI

# 加载 .env，优先项目根目录
PROJECT_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(PROJECT_ROOT / ".env")
load_dotenv(PROJECT_ROOT / ".env.local", override=True)

logger = logging.getLogger("deepseek")
logger.setLevel(logging.INFO)
if not logger.handlers:
    h = logging.StreamHandler(sys.stderr)
    h.setFormatter(logging.Formatter("[%(levelname)s] %(name)s: %(message)s"))
    logger.addHandler(h)


def _mask_key(key: str) -> str:
    """遮蔽 API key 日志输出"""
    if not key or len(key) < 8:
        return "***"
    return key[:4] + "****" + key[-4:]


def _get_client() -> OpenAI:
    api_key = os.getenv("DEEPSEEK_API_KEY")
    base_url = os.getenv("DEEPSEEK_BASE_URL")
    if not api_key:
        raise RuntimeError("DEEPSEEK_API_KEY 未设置，请在 .env 中配置")
    if not base_url:
        raise RuntimeError("DEEPSEEK_BASE_URL 未设置，请在 .env 中配置")
    logger.info("DeepSeek client initialized: base_url=%s, key=%s", base_url, _mask_key(api_key))
    return OpenAI(api_key=api_key, base_url=base_url)


_client = None


def _get_or_create_client() -> OpenAI:
    global _client
    if _client is None:
        _client = _get_client()
    return _client


def _model() -> str:
    return os.getenv("DEEPSEEK_MODEL", "deepseek-v4")


def _strip_json_fence(text: str) -> str:
    """去掉 ```json ... ``` 围栏"""
    text = text.strip()
    if text.startswith("```"):
        # 移除第一行的 ```json 或 ```
        text = re.sub(r"^```[a-zA-Z]*\s*\n?", "", text, count=1)
        # 移除最后的 ```
        text = re.sub(r"\n?```\s*$", "", text)
    return text.strip()


def _append_unresolved(entry: dict):
    """追加记录到 unresolved_items.yaml"""
    log_path = PROJECT_ROOT / "unresolved_items.yaml"
    existing = []
    if log_path.exists():
        try:
            with open(log_path, "r", encoding="utf-8") as f:
                data = yaml.safe_load(f)
                if isinstance(data, list):
                    existing = data
        except Exception:
            pass
    existing.append(entry)
    with open(log_path, "w", encoding="utf-8") as f:
        yaml.safe_dump(existing, f, allow_unicode=True, sort_keys=False)


def call_deepseek_json(
    system_prompt: str,
    user_prompt: str,
    schema_hint: dict | None = None,
    max_retries: int = 3,
    temperature: float = 0.1,
    max_tokens: int = 8192,
    chunk_context: dict | None = None,
) -> dict | None:
    """
    调用 DeepSeek-v4 API，要求返回合法 JSON。

    Args:
        system_prompt: 系统提示词
        user_prompt: 用户提示词（包含 chunk 文本）
        schema_hint: 可选的 JSON Schema，作为输出格式提示
        max_retries: JSON 解析失败重试次数
        temperature: 采样温度
        max_tokens: 最大输出 token
        chunk_context: chunk 上下文（paper_id, chunk_id 等），用于记录失败

    Returns:
        解析后的 dict，失败返回 None
    """
    client = _get_or_create_client()
    model = _model()

    # 构造消息
    messages = [{"role": "system", "content": system_prompt}]
    user_content = user_prompt
    if schema_hint:
        schema_str = json.dumps(schema_hint, ensure_ascii=False, indent=2)
        user_content += (
            "\n\n--- OUTPUT JSON SCHEMA ---\n"
            "请严格按照以下 JSON Schema 输出，不要添加任何额外文字：\n"
            + schema_str
        )
    messages.append({"role": "user", "content": user_content})

    last_error = None
    for attempt in range(1, max_retries + 1):
        try:
            logger.info(
                "Calling DeepSeek API: model=%s, attempt=%d/%d, temp=%.2f",
                model, attempt, max_retries, temperature,
            )
            response = client.chat.completions.create(
                model=model,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens,
            )
            raw = response.choices[0].message.content or ""
            logger.info("DeepSeek response length: %d chars", len(raw))

            # 尝试解析 JSON
            cleaned = _strip_json_fence(raw)
            try:
                result = json.loads(cleaned)
                logger.info("JSON parsed successfully on attempt %d", attempt)
                return result
            except json.JSONDecodeError as je:
                last_error = f"JSON decode error: {je}"
                logger.warning("Attempt %d: %s", attempt, last_error)
                if attempt < max_retries:
                    # 在重试时追加提示
                    messages.append({"role": "assistant", "content": raw})
                    messages.append({
                        "role": "user",
                        "content": (
                            f"你的上一次输出不是合法 JSON（错误：{je}）。"
                            f"请只输出合法 JSON，不要添加任何其他内容。"
                        ),
                    })
                continue

        except Exception as e:
            last_error = f"API call error: {e}"
            logger.error("Attempt %d: %s", attempt, last_error)
            if attempt < max_retries:
                continue

    # 所有重试失败
    error_entry = {
        "error": last_error,
        "timestamp": str(Path.cwd()),
    }
    if chunk_context:
        error_entry.update(chunk_context)
    _append_unresolved(error_entry)
    logger.error("All %d retries failed for chunk: %s", max_retries, json.dumps(chunk_context, ensure_ascii=False, default=str))
    return None
