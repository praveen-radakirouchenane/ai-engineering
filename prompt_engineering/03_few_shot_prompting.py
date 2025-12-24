from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

#Few shot prompting: Directly provide instructions to the model and also provide few examples to the model

FEW_SHOT_SYSTEM_PROMPT='''
You should only answer coding related questions, do not answer anything else.
If user asks something else just say sorry I can't help you with this.

Examples:
Q: what is sum of 3+4?
A: Sorry, I can't help you with this question.

Q: Hi, can you please help in writing a addition program in python?
A: Yes, of course! 
    def addition(a,b):
    return a+b

'''

response = client.chat.completions.create(
    model='gpt-4o-mini',
    messages=[
        {"role": "system", "content": FEW_SHOT_SYSTEM_PROMPT},
        #{"role": "user", "content": "Hey, tell me a joke"}
        {"role": "user", "content": "Hey, can you write a code to multiply two numbers in python"}
    ]
)

print("Few shot GPT response: ",response.choices[0].message.content)