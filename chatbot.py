from dotenv import load_dotenv

from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from config import (
    EMBEDDING_MODEL,
    LLM_MODEL,
    VECTORSTORE_PATH,
    TOP_K,
    TEMPERATURE,
)

from prompts import SYSTEM_PROMPT
from utils import format_docs
from services.reranker import rerank_documents

load_dotenv()

embeddings = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-en-v1.5",
    model_kwargs={"device": "cpu"},
    encode_kwargs={"normalize_embeddings": True},
)
llm = ChatGroq(
    model=LLM_MODEL,
    temperature=TEMPERATURE
)

prompt = ChatPromptTemplate.from_template(SYSTEM_PROMPT)

chain = prompt | llm | StrOutputParser()


def load_retriever():
    vectorstore = FAISS.load_local(
        VECTORSTORE_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )

    return vectorstore.as_retriever(
        search_kwargs={"k": 20}
    )


def ask_question(question, history=""):
    retriever = load_retriever()

    # Retrieve documents from FAISS
    docs = retriever.invoke(question)

    print("\n===== BEFORE RERANK =====")
    for i, doc in enumerate(docs, start=1):
        print(
            f"{i}. {doc.metadata.get('source')} | "
            f"Page {doc.metadata.get('page')}"
        )

    # Cross Encoder reranking
    docs = rerank_documents(
        question,
        docs,
        top_n=TOP_K
    )

    print("\n===== AFTER RERANK =====")
    for i, doc in enumerate(docs, start=1):
        print(
            f"{i}. {doc.metadata.get('source')} | "
            f"Page {doc.metadata.get('page')}"
        )

    context = format_docs(docs)

    answer = chain.invoke(
        {
            "history": history,
            "context": context,
            "question": question,
        }
    )

    return answer, docs