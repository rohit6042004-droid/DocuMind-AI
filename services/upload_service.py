import os

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings

from config import (
    UPLOAD_FOLDER,
    VECTORSTORE_PATH,
    EMBEDDING_MODEL,
    CHUNK_SIZE,
    CHUNK_OVERLAP,
)


def index_uploaded_files(uploaded_files):

    documents = []

    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

    for uploaded_file in uploaded_files:

        save_path = os.path.join(
            UPLOAD_FOLDER,
            uploaded_file.name
        )

        with open(save_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        loader = PyPDFLoader(save_path)

        docs = loader.load()

        for doc in docs:
            doc.metadata["source"] = uploaded_file.name

        documents.extend(docs)

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
    )

    chunks = splitter.split_documents(documents)

    embeddings = OllamaEmbeddings(
        model=EMBEDDING_MODEL
    )

    vectorstore = FAISS.from_documents(
        chunks,
        embeddings
    )

    vectorstore.save_local(
        VECTORSTORE_PATH
    )

    return len(chunks)