from google import genai
from dotenv import load_dotenv
import os
from pathlib import Path

# load .env from repo root (adjust if your .env is elsewhere)
env_path = Path(__file__).resolve().parents[1] / ".env"
load_dotenv(dotenv_path=env_path)

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise RuntimeError("GEMINI_API_KEY not set. Add it to .env or export it in your shell.")

client = genai.Client(
    api_key=api_key
)

response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents='Who are you?'
)

print(f"Gemini response: {response.text}")