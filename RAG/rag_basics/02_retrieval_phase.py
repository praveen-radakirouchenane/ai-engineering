from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()



# Vector Embeddings
embeddings_model = OpenAIEmbeddings(
    model="text-embedding-3-large"
)

vector_db = QdrantVectorStore.from_existing_collection(
    url='http://localhost:6333/',
    collection_name="learning_collection",
    embedding=embeddings_model
)

#Take user input

user_query = input('Hi 👋, How can I help you today?')

# Relevant chunks from the vector db
seach_results = vector_db.similarity_search(query=user_query)

context = "\n\n\n".join([f"Page content:{result.page_content} Page number: {result.metadata['page_label']} File Location: {result.metadata['source']}"
                           for result in seach_results])

SYSTEM_PROMPT = f"""
    - You are a helpful AI assistant who answers user query based on the available
    context retrieved from a PDF file along with page_contents and page number.
    - You should only answer the user based on the following context and navigate the 
    user to open the right page number to know more.

    Context:
    {context}

"""

response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role":"system", "content":SYSTEM_PROMPT},
            {"role":"user", "content":user_query}
        ]
    )

print(f'🤖 response: {response.choices[0].message.content}')
