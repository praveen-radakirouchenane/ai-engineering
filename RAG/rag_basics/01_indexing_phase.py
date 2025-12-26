from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from dotenv import load_dotenv

load_dotenv()

pdf_path = Path(__file__).parent / "ai_engineering.pdf"

print(f"path: {pdf_path}")

loader = PyPDFLoader(pdf_path)

docs = loader.load()

print(docs[1])

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=400
)

chunks = text_splitter.split_documents(documents=docs)

# Vector Embeddings
embeddings_model = OpenAIEmbeddings(
    model="text-embedding-3-large"
    
)

vector_store = QdrantVectorStore.from_documents(
    url='http://localhost:6333/',
    collection_name="learning_collection",
    embedding=embeddings_model,
    documents=chunks
)

print("Indexing of documents is completed...")