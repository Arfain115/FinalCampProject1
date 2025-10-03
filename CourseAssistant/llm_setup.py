from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.tools.tavily_search import TavilySearchResults

from config import load_keys

api_key, _, _ = load_keys()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0,
    google_api_key=api_key
)

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

prompt_template = """
You are an assistant who helps answer course-related questions.

If the answer is not in the context, say "I don't know".

Context:
{context}

Question:
{question}

Answer:
"""
prompt = PromptTemplate(input_variables=["context", "question"], template=prompt_template)
chain = LLMChain(llm=llm, prompt=prompt)

tavily = TavilySearchResults()
