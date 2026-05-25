"""Quick API connectivity test"""
import os, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from dotenv import load_dotenv
load_dotenv(Path(__file__).resolve().parent.parent / ".env")
from openai import OpenAI

api_key = os.getenv("DEEPSEEK_API_KEY")
base_url = os.getenv("DEEPSEEK_BASE_URL")
model = os.getenv("DEEPSEEK_MODEL")

print(f"Base URL: {base_url}")
print(f"Model: {model}")
print(f"Key: {api_key[:8]}...")

client = OpenAI(api_key=api_key, base_url=base_url)
response = client.chat.completions.create(
    model=model,
    messages=[{"role": "user", "content": "Say hello in 5 words"}],
    max_tokens=50,
)
print(f"Response: {response.choices[0].message.content}")
print("API connection OK")
