from openai import OpenAI
from dotenv import load_dotenv
import json

load_dotenv()

client = OpenAI()

#Chain-of-thought prompting

COT_SYSTEM_PROMPT="""
ROLE:
    - You're an expert AI Assistant in resolving user queries using chain of thought.
    - You work on START, PLAN and OUTPUT steps.
    - You need to first PLAN what needs to be done. The PLAN can be multiple steps.
    - Once you think enough PLAN has been done, finally you can give an OUTPUT.
Rules:
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

response = client.chat.completions.create(
    model='gpt-4o-mini',
    response_format={"type":"json_object"},
    messages=[
        {"role": "system", "content": COT_SYSTEM_PROMPT},
        
        { "role": "user", "content": "Hey, write a code to add n numbers in js"},
        
        { "role": "assistant", "content": json.dumps({"step": "PLAN", "content": "User wants to create a JavaScript code to add a variable number of integers."})},
        
        {
        "role": "assistant",
        "content": json.dumps({
            "step": "PLAN",
            "content": "To achieve this, I need to consider using a function that accepts an array of numbers."
        })
        },

        {
        "role": "assistant",
        "content": json.dumps({
            "step": "PLAN",
            "content": "The function can use the reduce method to sum up all the elements in the array."
        })
        },

        {
        "role": "assistant",
        "content": json.dumps({
            "step": "PLAN",
            "content": "I also need to include an example of how to call this function with a sample array of numbers."
        })
        }

    ]
)

print("COT GPT response: ",response.choices[0].message.content)


#{"step": "OUTPUT", "content": "Here's the JavaScript code to add n numbers:\n\nfunction addNumbers(numbers) "
#"{\n    return numbers.reduce((accumulator, current) => accumulator + current, 0);\n}\n\n// Example usage:\nconst result = addNumbers([1, 2, 3, 4, 5]);\nconsole.log(result); // Output will be 15"}

