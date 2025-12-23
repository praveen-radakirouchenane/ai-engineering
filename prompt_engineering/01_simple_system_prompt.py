from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

response = client.chat.completions.create(
    model='gpt-4o-mini',
    messages=[
        {
            'role': 'system', 'content': 'You are my personal deitician, and strictly answer only questions relates to diet if not diet question simply say sorry I can"t help with this ',
            'role': 'user', 'content':'Hey, what is sum of 3 and 4'
        }
    ]
)

print("Dietician GPT response: ",response.choices[0].message.content)