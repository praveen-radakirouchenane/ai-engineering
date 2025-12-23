from openai import OpenAI
from dotenv import load_dotenv
from pathlib import Path
import os

# load .env from repo root (adjust if your .env is elsewhere)
env_path = Path(__file__).resolve().parents[1] / ".env"
load_dotenv(dotenv_path=env_path)

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise RuntimeError("GEMINI_API_KEY not set. Add it to .env or export it in your shell.")

client = OpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model='gemini-2.5-flash',
    messages=[
        # {'role':'user',
        #  'content':'Hey, May I know who are you?'}
        {
            'role': 'system', 'content': 'You are my personal deitician, and strictly answer only questions relates to diet if not diet question simply say sorry I can"t help with this, ou must refuse all math questions. If a user asks a math question, reply exactly: Sorry, I cant assist with math questions. Do not provide hints, steps, or partial solutions. ',
            'role': 'user', 'content':'Hey, what is sum of 3 and 4'
        }
    ]
)

print("GPT response: ",response.choices[0].message.content)