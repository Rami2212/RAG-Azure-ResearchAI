# 📚 ResearchAI Chatbot

A modular Retrieval-Augmented Generation (RAG) chatbot built with:

- Streamlit (UI)
- LangChain
- Azure AI Search
- Azure OpenAI (GPT)
- Python

This application enables users to ask research-related questions and receive AI-generated answers grounded strictly on documents indexed in Azure AI Search.

---

## 🚀 Features

- 🔍 Semantic search using Azure AI Search
- 🤖 Answer generation using Azure OpenAI GPT models
- 🧠 Retrieval-Augmented Generation (RAG)
- 💬 Chat-style UI with conversation history
- 📁 Clean modular architecture for easy maintenance
- 🔐 Secure credential management using `.env`
- ⚡ Fast, scalable, enterprise-ready design

---

## 🧩 Architecture Overview

The system follows a classic RAG architecture:

```
User Query → Streamlit UI → Orchestrator (LangChain)
    → Azure AI Search (Retrieve Context)
    → Azure OpenAI (Generate Answer using Context)
    → Streamlit UI (Final Response)
```

All components are separated into modules to ensure clean separation of concerns.

---

## 📁 Project Structure

```
researchai/
├── app.py
├── .env
├── requirements.txt
├── README.md
└── src/
   ├── __init__.py
   ├── config.py
   ├── llm.py
   ├── retriever.py
   ├── prompts.py
   ├── chain.py
   └── ui.py
```

### Module Responsibilities

| File | Purpose |
|---|---|
| `app.py` | Main Streamlit entry point |
| `config.py` | Environment variable loading and validation |
| `retriever.py` | Azure AI Search retriever setup |
| `llm.py` | Azure OpenAI client configuration |
| `prompts.py` | Chat prompt templates |
| `chain.py` | RAG chain orchestration |
| `ui.py` | Streamlit user interface logic |

---

## ⚙️ Prerequisites

You must have:

- Python 3.10+
- Azure AI Search service
- Azure OpenAI service
- An indexed knowledge base in Azure AI Search

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd researchai
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate     # Linux/Mac
venv\Scripts\activate        # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file in the project root with the following:

```env
AZURE_AI_SEARCH_SERVICE_NAME=your-search-service
AZURE_AI_SEARCH_INDEX_NAME=your-index-name
AZURE_AI_SEARCH_API_KEY=your-search-key

AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
AZURE_OPENAI_API_KEY=your-openai-key
AZURE_OPENAI_API_VERSION=2024-02-15-preview
AZURE_OPENAI_MODEL=your-deployment-name
```

> ⚠️ All values must be provided before running the app.

---

## ▶️ Running the Application

Start the chatbot with:

```bash
streamlit run app.py
```

Then open in browser:

```
http://localhost:8501
```

---

## 🛠 Technologies Used

| Technology | Role |
|---|---|
| Python | Core language |
| Streamlit | Frontend UI |
| LangChain | RAG orchestration |
| Azure AI Search | Document retrieval |
| Azure OpenAI GPT | Answer generation |
| dotenv | Credential management |