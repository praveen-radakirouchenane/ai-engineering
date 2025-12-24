from openai import OpenAI
from dotenv import load_dotenv
import json

load_dotenv()

client = OpenAI()

#Chain-of-thought prompting

COT_SYSTEM_PROMPT="""
ROLE:
    - You're an expert AI Assistant in solving math problem by resolving user queries using chain of thought.
    - You work on START, PLAN and OUTPUT steps.
    - You need to first PLAN what needs to be done. The PLAN can be multiple steps.
    - Once you think enough PLAN has been done, finally you can give an OUTPUT.
Rules:
- You should not answer any random question, and answer only relates to MATH
- If user asks any non releated MATH question politely say sorry, I can't help with this.
- Strictly follow the given JSON output format
- Only run one step at a time.
- The sequence of steps is START (where user gives an input), PLAN (That can be multiple times) and finally OUTPUT (which is going to the displayed to the user).

Output JSON Format:
    { "step": "START" | "PLAN" | "OUTPUT", "content": "string" }  

Example:
    START: Hey, Can you solve 2 + 3 * 5 / 10
    PLAN: { "step": "PLAN", "content": "Seems like user is interested in math problem" }
    PLAN: { "step": "PLAN", "content": "looking at the problem, we should solve this using BODMAS method" }
    PLAN: { "step": "PLAN", "content": "Yes, The BODMAS is correct thing to be done here" }
    PLAN: { "step": "PLAN", "content": "first we must multiply 3 * 5 which is 15" }
    PLAN: { "step": "PLAN", "content": "Now the new equation is 2 + 15 / 10" }
    PLAN: { "step": "PLAN", "content": "We must perform divide that 15/10 which is 1.5" }
    PLAN: { "step": "PLAN", "content": "Now the new equation is 2 + 1.5" }
    OUTPUT: { "step": "OUTPUT", "content": "3.5" }
"""
print("\n"*3)
print("=="*50)
print("\n"*2)

user_query = input('Hi 👋, How can I help you today? ') 

print("\n"*2)

message_history = [
       {"role": "system", "content": COT_SYSTEM_PROMPT}
]

message_history.append(
    {"role":"user", "content":user_query}
    )

while True:

    response = client.chat.completions.create(
        model='gpt-4o-mini',
        response_format={"type":"json_object"},
        messages= message_history
    )
    raw_response = response.choices[0].message.content
    raw_response_parse = json.loads(raw_response)
    message_history.append({"role":"assistant", "content":raw_response})

    if raw_response_parse.get('step') == 'START':
        content = raw_response_parse.get("content")
        print("🔥",content)
        if 'sorry' in content.lower():
            break
        continue

    if raw_response_parse.get('step') == 'PLAN':
        print("🧠",raw_response_parse.get("content"))
        continue

    if raw_response_parse.get('step') == 'OUTPUT':
        print("🤖",raw_response_parse.get("content"))
        break

print("\n"*3)
print("=="*50)


#Examples 1: Hi 👋, How can I help you today? can you tell me joke
#Examples 2: can you help me in solving the following 3*4*7/9*3
