# 📘 Course Assistant (RAG + Web Search)

This project is a smart assistant that answers course-related questions using:
- **PDF documents** (RAG with Pinecone)
- **Fallback web search** (Tavily)

It uses **LangChain**, **Gemini (Google Generative AI)**, and **Pinecone** for vector storage.

---

## 🚀 Features
- Upload and process course catalog PDFs.
- Store document embeddings in Pinecone.
- Ask natural language questions.
- Answers from PDF if found, otherwise falls back to web search.

---

## ⚙️ Setup
1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/course-assistant.git
   cd course-assistant

2. Store Dependencies:
pip install -r requirements.txt

3. Set environment variables (or load via Colab userdata):
export GOOGLE_API_KEY="google_api_key"
export PINECONE_API_KEY="pinecone_api_key"
export TAVILY_API_KEY="tavily_api_key"

4. Run Assistant:
python main.py
