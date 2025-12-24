from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

#Few shot prompting: Directly provide instructions to the model and also provide few examples to the model

FEW_SHOT_SYSTEM_PROMPT='''
Role:
You're my coding assistant, and you should only answer coding related questions, do not answer anything else.
If user asks something else just say sorry I can't help you with this.

Rule:
- Strictly provide the output in JSON format

Output Format:
- {{
    'code': string or null,
    'isCodingQuestion': boolean
}}

Examples:
Q: what is sum of 3+4?
A: Sorry, I can't help you with this question.
{{
    'code': null,
    'isCodingQuestion': false
}}

Q: Hi, can you please help in writing a addition program in python?
A: 

{{
    'code': '
    def addition(a,b):
    return a+b',
    'isCodingQuestion': true
}}

'''

response = client.chat.completions.create(
    model='gpt-4o-mini',
    messages=[
        {"role": "system", "content": FEW_SHOT_SYSTEM_PROMPT},
        {"role": "user", "content": "Hey, tell me a joke"}
        #{"role": "user", "content": "Hey, can you write a code to add two numbers in javascript"}
    ]
)

print("Few shot GPT response: ",response.choices[0].message.content)