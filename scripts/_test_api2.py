"""Quick API test with JSON output"""
import os, sys, json
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from dotenv import load_dotenv
load_dotenv(Path(__file__).resolve().parent.parent / ".env")
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url=os.getenv("DEEPSEEK_BASE_URL"),
)
model = os.getenv("DEEPSEEK_MODEL")

response = client.chat.completions.create(
    model=model,
    messages=[
        {"role": "system", "content": "Output only valid JSON."},
        {"role": "user", "content": 'Return: {"status":"ok","test":true}'}
    ],
    max_tokens=100,
    temperature=0,
)
content = response.choices[0].message.content
print(f"Raw response ({len(content) if content else 0} chars): {repr(content[:200])}")

# Check finish reason
print(f"Finish reason: {response.choices[0].finish_reason}")
print(f"Model used: {response.model}")
