from dotenv import load_dotenv
from typing_extensions import TypedDict
from typing import Optional, Literal
from langgraph.graph import StateGraph, START, END
from langchain_openai import ChatOpenAI
from openai import OpenAI

load_dotenv()

client = OpenAI()

class State(TypedDict):
    user_query:str
    llm_output: Optional[str]
    is_good: Optional[bool]

def chatbot(state: State):
    print("Chatbot Node", state)
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role":"user", "content":state.get("user_query")}
        ]
    )
    state["llm_output"] = response.choices[0].message.content
    return state

def evaluation_response(state: State) -> Literal["chatbot_gemini", "endnode"]:
    print("Evaluation_response Node", state)
    if True:
        return "endnode"
    # if False:
    #     return "endnode"
    
    return "chatbot_gemini"


def chatbot_gemini(state: State):
    print("Chatbot_gemini Node", state)
    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[
            {"role":"user", "content":state.get("user_query")}
        ]
    )
    state["llm_output"] = response.choices[0].message.content
    return state

def endnode(state: State):
    print("Endnode Node", state)
    return state

graph_builder = StateGraph(State)

graph_builder.add_node("chatbot",chatbot)
graph_builder.add_node("chatbot_gemini",chatbot_gemini)
graph_builder.add_node("endnode",endnode)


graph_builder.add_edge(START,"chatbot")
graph_builder.add_conditional_edges("chatbot",evaluation_response)

graph_builder.add_edge("chatbot_gemini","endnode")
graph_builder.add_edge("endnode",END)


graph = graph_builder.compile()

updated_state = graph.invoke(State({"user_query":"Hey, What is 3 * 4?"}))

print("Updated state: ", updated_state)


#Usecase 1(evaluation_response -> True):
# Chatbot Node {'user_query': 'Hey, What is 3 * 4?'}
# Evaluation_response Node {'user_query': 'Hey, What is 3 * 4?', 'llm_output': '3 * 4 is 12.'}
# Endnode Node {'user_query': 'Hey, What is 3 * 4?', 'llm_output': '3 * 4 is 12.'}
# Updated state:  {'user_query': 'Hey, What is 3 * 4?', 'llm_output': '3 * 4 is 12.'}

#Usecase 2(evaluation_response -> False):
# Chatbot Node {'user_query': 'Hey, What is 3 * 4?'}
# Evaluation_response Node {'user_query': 'Hey, What is 3 * 4?', 'llm_output': '3 * 4 = 12'}
# Chatbot_gemini Node {'user_query': 'Hey, What is 3 * 4?', 'llm_output': '3 * 4 = 12'}
# Endnode Node {'user_query': 'Hey, What is 3 * 4?', 'llm_output': '3 * 4 = **12**'}
# Updated state:  {'user_query': 'Hey, What is 3 * 4?', 'llm_output': '3 * 4 = **12**'}