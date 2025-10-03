from pdf_processor import load_and_split_pdf
from vector_store import setup_vector_store
from llm_setup import llm, chain, tavily
from qa import smart_answer
from config import load_keys

def main():
    # Load API keys
    load_keys()

    # Upload & process PDF
    docs = load_and_split_pdf()

    # Setup Pinecone vector store
    vector_store = setup_vector_store(docs)

    # Test queries
    print(smart_answer("List all the undergraduate programs.", vector_store, chain, llm, tavily))
    print(smart_answer("What is new in Python 3.12?", vector_store, chain, llm, tavily))

if __name__ == "__main__":
    main()
