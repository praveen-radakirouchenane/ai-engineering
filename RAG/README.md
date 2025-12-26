# Start the following

# Qdrant
    cd RAG/rag_basics
    docker compose up -d

# ValKey
    cd RAG/rag_queue
    docker compose up -d
    http://localhost:6333/dashboard#/collections

# FastAPI
    cd RAG/
    python -m rag_queue.main
    http://localhost:8080/docs


## Workers
    cd RAG/
    export OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES
    rq worker

Note: You can create multiple terminal to run multiple workers by executing above command to process parallel user queries


## References
1. https://python-rq.org/

