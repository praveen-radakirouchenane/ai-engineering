from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

response = client.chat.completions.create(
    model='gpt-4o-mini',
    messages=[
        {'role':'user',
         'content':'Hey, Myself PK, how are you? and, how is weather outside?'}
    ]
)

print("GPT response: ",response.choices[0].message.content)