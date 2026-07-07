from dotenv import load_dotenv
from services.hybrid_search import hybrid_search

from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from config import LLM_MODEL, VECTORSTORE_PATH, TOP_K, TEMPERATURE
from prompts import SYSTEM_PROMPT
from utils import format_docs
from services.reranker import rerank_documents

load_dotenv()

embeddings = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-en-v1.5",
    model_kwargs={"device": "cpu"},
    encode_kwargs={"normalize_embeddings": True},
)

llm = ChatGroq(model=LLM_MODEL, temperature=TEMPERATURE)

prompt = ChatPromptTemplate.from_template(SYSTEM_PROMPT)

chain = prompt | llm | StrOutputParser()


def load_vectorstore():
    return FAISS.load_local(
        VECTORSTORE_PATH,
        embeddings,
        allow_dangerous_deserialization=True,
    )


def retrieve_documents(question, selected_document="All Documents"):
    vectorstore = load_vectorstore()

    if selected_document != "All Documents":
        docs = vectorstore.similarity_search(
            question,
            k=30,
            filter={"source": selected_document},
        )
    else:
       docs = hybrid_search(question,vectorstore,selected_document,k=30)

    docs = rerank_documents(question, docs, top_n=TOP_K)

    return docs


def ask_question(question, history="", selected_document="All Documents"):
    docs = retrieve_documents(question, selected_document)

    context = format_docs(docs)

    answer = chain.invoke(
        {
            "history": history,
            "context": context,
            "question": question,
        }
    )

    return answer, docs