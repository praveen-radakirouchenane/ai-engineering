from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

ZERO_SHOT_SYSTEM_PROMPT="You are my personal math assistant, and strictly answer only questions relates to math if not math question simply say sorry I cant help with this"

response = client.chat.completions.create(
    model='gpt-4o-mini',
    messages=[
        {
            "role": "system", "content": ZERO_SHOT_SYSTEM_PROMPT,
            # 'role': 'user', 'content':'Hey, what is sum of 3 and 4'
              "role": "system", "content": "Hey, tell me a joke"
        }
    ]
)

print("MATH GPT response: ",response.choices[0].message.content)