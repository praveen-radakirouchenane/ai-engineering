from openai import OpenAI
from dotenv import load_dotenv
import requests
import json
from typing import Optional
from pydantic import BaseModel, Field

load_dotenv()

client = OpenAI()


#Chain-of-thought prompting

COT_SYSTEM_PROMPT="""
ROLE:
    - You're an expert AI Assistant in resolving user queries using chain of thought.
    - You work on START, PLAN and OUTPUT steps.
    - You need to first PLAN what needs to be done. The PLAN can be multiple steps.
    - Once you think enough PLAN has been done, finally you can give an OUTPUT.
    - You can also call a tool if required from the list of available tools. 
    - For every tool call wait for the observe step which is teh output from the called tool.

Rules:
- Strictly follow the given JSON output format
- Only run one step at a time.
- The sequence of steps is START (where user gives an input), PLAN (That can be multiple times) and finally OUTPUT (which is going to the displayed to the user).

Output JSON Format:
    { "step": "START" | "PLAN" | "OUTPUT" | "TOOL" | "OBSERVE", "content": "string", "tool": "string", "input":"string" }  

Available Tools:
    - get_weather(city:str): Takes city name as input string and returns the weather info about the city

Example 1:
    START: Hey, Can you solve 2 + 3 * 5 / 10
    PLAN: { "step": "PLAN", "content": "Seems like user is interested in math problem" }
    PLAN: { "step": "PLAN", "content": "looking at the problem, we should solve this using BODMAS method" }
    PLAN: { "step": "PLAN", "content": "Yes, The BODMAS is correct thing to be done here" }
    PLAN: { "step": "PLAN", "content": "first we must multiply 3 * 5 which is 15" }
    PLAN: { "step": "PLAN", "content": "Now the new equation is 2 + 15 / 10" }
    PLAN: { "step": "PLAN", "content": "We must perform divide that 15/10 which is 1.5" }
    PLAN: { "step": "PLAN", "content": "Now the new equation is 2 + 1.5" }
    OUTPUT: { "step": "OUTPUT", "content": "3.5" }

Example 2:
    START: Hey, What is the weather of Sydney?
    PLAN: { "step": "PLAN", "content": "Seems like user is interested in getting weather of Sydney in Australia" }
    PLAN: { "step": "PLAN", "content": "Let's see if we have any available tools from the list of available tools" }
    PLAN: { "step": "PLAN", "content": "Great, we have get_weather tool available for this query" }
    PLAN: { "step": "PLAN", "content": "I need to call get_weather tool for Sydney as input for city" }
    PLAN: { "step": "TOOL", "tool": "get_weather", "input":"Sydney" }
    PLAN: { "step": "OBSERVE", "tool": "get_weather", "output":"The temperature of Sydney is Overcast with +20 C" }
    PLAN: { "step": "PLAN", "content": "Great, I got the weather info about Sydney" }
    OUTPUT: { "step": "OUTPUT", "content": "The current weather in Sydney is 20 C with Overcast condition" }
"""

class OutputFormat(BaseModel):
    step: str = Field(..., description="The ID of the step. Example: PLAN, OUTPUT, TOOL")
    content: Optional[str] = Field(None, description="The optional string for the step")
    tool: Optional[str] = Field(None, description="The ID of the tool to call")
    input: Optional[str] = Field(None, description="The input params for the tool")



def get_weather(city:str):
    url = f"https://wttr.in/{city.lower()}?format=%C+%t"
    response = requests.get(url)
    
    if response.status_code == 200:
        return f"Current weather for the city {city.upper()} is {response.text}"
    
    return f"Something went wrong. Please try again"


available_tools = {    "get_weather": get_weather}


while True: 
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

        response = client.chat.completions.parse(
            model='gpt-4o-mini',
            response_format= OutputFormat,
            messages= message_history
        )
        raw_response = response.choices[0].message.content
        raw_response_parse = response.choices[0].message.parsed

        message_history.append({"role":"assistant", "content":raw_response})

        if raw_response_parse.step == 'START':
            content = raw_response_parse.content
            print("🔥",content)
            if 'sorry' in content.lower():
                break
            continue

        if raw_response_parse.step == 'PLAN':
            print("🧠",raw_response_parse.content)
            continue

        if raw_response_parse.step == 'TOOL':
            tool_to_call = raw_response_parse.tool
            tool_input = raw_response_parse.input
            print(f"⚒️: {tool_to_call}({tool_input})")

            tool_response = available_tools[tool_to_call](tool_input)
            print(f"⚒️: {tool_to_call} ({tool_input}) = {tool_response}")
            message_history.append({"role":"developer", "content": json.dumps(
                {"step": "OBSERVE", "tool": tool_to_call, "input": tool_input, "output": tool_response}
            )})
            continue

        if raw_response_parse.step == 'OUTPUT':
            print("🤖",raw_response_parse.content)
            break


# Example user questions:
#1. What is the weather is Delhi?
#2. What is the temperature in London, and Manchester?
#3. what is weather of all capital cities in Australia