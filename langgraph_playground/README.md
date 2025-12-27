### Langraph
LangGraph is an open-source orchestration framework designed for building, managing, and deploying complex, stateful AI agent workflows.

## What is Langraph?

#Core Architecture

LangGraph represents applications as directed graphs where: 

    #Nodes: Represent individual steps or units of work, such as calling an LLM, executing a tool, or running custom Python code.
    
    #Edges: Define the transition paths between nodes. These can be fixed or conditional, where the next step depends on the current state (e.g., if-else logic).
    
    #State: A shared data structure (dictionary or Pydantic model) that is updated as the agent moves through the graph, ensuring context is maintained throughout the process. 

## Setup
    - pip install -U langgraph
