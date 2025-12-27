from dotenv import load_dotenv
from typing_extensions import TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END
from langchain_openai import ChatOpenAI


load_dotenv()


llm = ChatOpenAI(model="gpt-4o-mini")


class State(TypedDict):
    messages: Annotated[list, add_messages]


def chat_bot(state: State):
    response = llm.invoke(state.get("messages"))
    return {"messages": [response]}

def knowledge_bot(state: State):
    print("\n\nInside Knowledge Bot Node", state)
    return {"messages": ["Hi, I am your KnowledgeBot Node"]}


graph_builder = StateGraph(State)

graph_builder.add_node("chatbot",chat_bot)
graph_builder.add_node("knowledgebot",knowledge_bot)

# START -> Chatbot -> KnowledgeBot -> END

graph_builder.add_edge(START,"chatbot")
graph_builder.add_edge("chatbot","knowledgebot")
graph_builder.add_edge("knowledgebot",END)

graph = graph_builder.compile()

final_state = graph.invoke(State({"messages":"Hi, Myself Praveen starting the Graph"}))
print("\n\n Final state", final_state)


