import os
from google.colab import userdata

def load_keys():
    api_key = userdata.get("GOOGLE_API_KEY")
    pinecone_api_key = userdata.get("PINECONE_API_KEY")
    tavily_api_key = userdata.get("TAVILY_API_KEY")

    os.environ["GOOGLE_API_KEY"] = api_key or ""
    os.environ["PINECONE_API_KEY"] = pinecone_api_key or ""
    os.environ["TAVILY_API_KEY"] = tavily_api_key or ""

    print("Gemini key loaded:", bool(api_key))
    print("Pinecone key loaded:", bool(pinecone_api_key))
    print("Tavily key loaded:", bool(tavily_api_key))

    return api_key, pinecone_api_key, tavily_api_key
