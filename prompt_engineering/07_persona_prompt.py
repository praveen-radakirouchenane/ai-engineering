from openai import OpenAI
from dotenv import load_dotenv
import json

load_dotenv()

client = OpenAI()

#Persona prompting

Persona_SYSTEM_PROMPT= """
    You are the personal AI assistant for Praveen, who is an software engineer working in Sydney
    You should answer all my software related questions
    At time you are allowed to tell jokes but not anything else

    examples:
    Q: Hey, write code to add two numbers in python
    A: Yes, sure 
"""
 
response = client.chat.completions.create(
        model='gpt-4o-mini',
        messages= [
            {"role":"system", "content":Persona_SYSTEM_PROMPT},
            {"role":"user", "content":"Who are you?"}
        ]
    )
raw_response = response.choices[0].message.content

print(f"Persona GPT reponse: {raw_response}")