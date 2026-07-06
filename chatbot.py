from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from services.reranker import rerank_documents
load_dotenv()

from config import (
    EMBEDDING_MODEL,
    LLM_MODEL,
    VECTORSTORE_PATH,
    TOP_K,
    TEMPERATURE,
)

from prompts import SYSTEM_PROMPT
from utils import format_docs


# Load models only once
embeddings = OllamaEmbeddings(model=EMBEDDING_MODEL)

vectorstore = FAISS.load_local(
    VECTORSTORE_PATH,
    embeddings,
    allow_dangerous_deserialization=True
)

retriever = vectorstore.as_retriever(
    search_kwargs={"k": 15}
)

llm = ChatGroq(
    model=LLM_MODEL,
    temperature=TEMPERATURE
)

prompt = ChatPromptTemplate.from_template(SYSTEM_PROMPT)

chain = prompt | llm | StrOutputParser()


def ask_question(question, history=""):
    """
    Ask a question to the RAG system.

    Returns:
        answer
        retrieved_docs
    """

    docs = retriever.invoke(question)
    docs = rerank_documents(question, docs, top_n=4)

    context = format_docs(docs)

    answer = chain.invoke(
        {
            "history": history,
            "context": context,
            "question": question,
        }
    )

    return answer, docs