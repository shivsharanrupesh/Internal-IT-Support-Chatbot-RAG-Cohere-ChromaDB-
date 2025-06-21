# Internal-IT-Support-Chatbot-RAG-Cohere-ChromaDB-

A next-gen, Retrieval-Augmented Generation (RAG) chatbot for instant, reliable IT support—using your company's official PDF knowledge base.

📖 Table of Contents
Overview

Architecture

Features

Project Structure

Setup

Usage

How It Works

Troubleshooting

Extending

Security

Credits

📝 Overview
This project provides a production-ready RAG chatbot that answers employees’ IT and tech support questions by searching your company’s PDF documentation.

No more waiting for a helpdesk agent!

All answers come from your company’s own docs (never hallucinated, always transparent).

🏗️ Architecture
PDF Ingestion:
Parses/splits PDFs from /data and creates semantic embeddings with Cohere.

Vector Store:
Stores and searches document chunks using ChromaDB.

RAG Pipeline:
Combines retrieval (via embeddings) and generative AI (Cohere LLM).

Chat Memory:
Multi-turn chat with session memory (via mem0).

APIs:
Backend (FastAPI) and web chat frontend (Streamlit).

✨ Features
Instant answers for IT issues using company-approved docs only.

Source referencing—shows which PDF and page the answer came from.

Multi-turn conversation—remembers context per session.

Fully local, secure, and extendable.

No hardcoded secrets—all keys via environment variables.

📂 Project Structure
graphql
Copy
Edit
rag-it-support-chatbot/
├── app/
│   ├── ingest.py        # PDF loader, chunker, embedder, vectorstore builder
│   ├── rag_chain.py     # RAG pipeline: Retriever + LLM + Memory
│   └── api.py           # FastAPI backend (/ask endpoint)
├── chat_ui.py           # Streamlit chat UI
├── requirements.txt     # All dependencies
├── README.md
├── data/                # Put your company PDFs here
└── memory_store/        # Created at runtime for session memory
⚙️ Setup
Requirements:

Python 3.9+

Cohere API Key

IT documentation as PDF in /data

1. Clone and Install
sh
Copy
Edit
git clone https://github.com/your-org/rag-it-support-chatbot.git
cd rag-it-support-chatbot
pip install -r requirements.txt
2. Configure Environment
sh
Copy
Edit
# Set your Cohere API Key
export COHERE_API_KEY=your-cohere-api-key      # Linux/macOS
set COHERE_API_KEY=your-cohere-api-key         # Windows

# Optional: Set persistent vector store directory
export CHROMA_DB_DIR=your/path/to/vectorstore
3. Add IT PDFs
Put your company’s FAQ, policy, and troubleshooting PDFs in data/.

4. Ingest Documents
sh
Copy
Edit
python app/ingest.py
5. Start Backend API
sh
Copy
Edit
uvicorn app.api:app --reload
6. Start Frontend (Chat UI)
sh
Copy
Edit
streamlit run chat_ui.py
🚀 Usage
Open http://localhost:8501 in your browser.

Type your IT support question.

See answers pulled from company documentation—with sources and context!

Multi-turn (conversational) support: the bot remembers previous chat for your session.

🧠 How It Works
Question asked:
Employee asks a question via Streamlit UI.

Chunk retrieval:
System finds relevant PDF chunks via ChromaDB and Cohere embeddings.

RAG chain:
Cohere LLM receives both the question and retrieved document context to generate a reliable answer.

References:
The bot always cites which PDF(s) and page(s) were used for each answer.

Session memory:
Each chat is tracked via unique session ID, preserving context and history.

🛠️ Troubleshooting
No PDFs found:
Ensure at least one .pdf file exists in /data.

Cohere API errors:
Make sure COHERE_API_KEY is set in your environment.

Vectorstore not persistent:
Set CHROMA_DB_DIR to a directory for disk persistence.

Streamlit cannot connect:
Confirm FastAPI backend is running at localhost:8000.

🧩 Extending
Add authentication (SSO/LDAP) for personalized experience.

Integrate escalation to human IT agents.

Add analytics for support trends.

Support more document formats (Word, HTML).

Containerize for easy deployment (add Docker support).

🔐 Security
No API keys are ever committed—always use environment variables.

All answers and context are strictly sourced from your private company docs.

🙏 Credits
LangChain

ChromaDB

Cohere

Streamlit

mem0
