from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from llm_setup import embeddings
from config import load_keys

def setup_vector_store(docs):
    _, pinecone_api_key, _ = load_keys()
    pc = Pinecone(api_key=pinecone_api_key)
    index_name = "courses-index"

    if index_name not in [i["name"] for i in pc.list_indexes()]:
        pc.create_index(
            name=index_name,
            dimension=384,
            metric="cosine",
            spec=ServerlessSpec(cloud="aws", region="us-east-1")
        )
        print("Created new Pinecone index:", index_name)

    vector_store = PineconeVectorStore.from_documents(
        documents=docs,
        embedding=embeddings,
        index_name=index_name
    )
    print("Documents stored in Pinecone ✅")
    return vector_store
