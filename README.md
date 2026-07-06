# 🤖 DocuMind AI

> AI-powered document intelligence platform that allows users to upload PDFs, ask natural language questions, and receive source-grounded answers using Retrieval-Augmented Generation (RAG).

---

## 🚀 Features

- 📂 Upload and index PDF documents
- 💬 Chat with your documents using AI
- 🔍 Semantic search with FAISS
- 🧠 Groq-powered Llama LLM
- 📖 Source citations with page references
- ⚡ Fast document retrieval
- 🔄 Automatic PDF indexing
- 🏗️ Modular architecture for easy extension
- 🎯 Cross Encoder Re-ranking (in progress)

---

## 🏗️ Architecture

```text
                User
                  │
                  ▼
           Streamlit UI
                  │
                  ▼
        Upload / Ask Question
                  │
                  ▼
        Document Chunking
                  │
                  ▼
      Ollama Embeddings
                  │
                  ▼
        FAISS Vector Store
                  │
                  ▼
      Cross Encoder (Re-ranking)
                  │
                  ▼
        Groq Llama 3.3 API
                  │
                  ▼
        Source-grounded Answer
```

---

## 🛠️ Tech Stack

- Python
- Streamlit
- LangChain
- FAISS
- Groq API
- Llama 3.3
- Ollama Embeddings
- Sentence Transformers
- PyPDF
- Cross Encoder Re-ranking

---

## 📂 Project Structure

```text
DocuMind-AI
│
├── app.py
├── chatbot.py
├── config.py
├── ingest.py
├── pages.py
├── prompts.py
├── requirements.txt
├── utils.py
│
├── services
│   ├── upload_service.py
│   └── reranker.py
│
├── uploads
├── vectorstore
├── assets
└── README.md
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/rohit6042004-droid/DocuMind-AI.git
cd DocuMind-AI
```

### Create virtual environment

```bash
python -m venv venv
```

### Activate environment

Windows

```bash
venv\Scripts\activate
```

Mac/Linux

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Configure API Key

Create a `.env` file:

```text
GROQ_API_KEY=your_api_key_here
```

### Run the application

```bash
streamlit run app.py
```

---

## 💡 How it Works

1. Upload one or more PDF documents.
2. Documents are split into semantic chunks.
3. Chunks are converted into vector embeddings.
4. FAISS retrieves the most relevant chunks.
5. A Cross Encoder reranks retrieved chunks.
6. Groq's Llama model generates an answer using the reranked context.
7. Source pages are displayed for transparency.

---

## 📈 Future Improvements

- Multi-document management
- Hybrid Search (BM25 + FAISS)
- AI-generated document summaries
- Quiz generation
- Flashcards
- Compare multiple PDFs
- Chat history
- REST API using FastAPI
- Docker deployment

---

## 👨‍💻 Author

**Rohit Singh**

GitHub: https://github.com/rohit6042004-droid

---

## ⭐ If you found this project useful

Please consider giving it a ⭐ on GitHub.
