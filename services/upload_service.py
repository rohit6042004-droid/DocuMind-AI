import os

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

from config import (
    UPLOAD_FOLDER,
    VECTORSTORE_PATH,
    CHUNK_SIZE,
    CHUNK_OVERLAP,
)

embeddings = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-en-v1.5",
    model_kwargs={"device": "cpu"},
    encode_kwargs={"normalize_embeddings": True},
)


def load_vectorstore():
    """
    Load existing FAISS index if present.
    """

    if os.path.exists(VECTORSTORE_PATH):

        return FAISS.load_local(
            VECTORSTORE_PATH,
            embeddings,
            allow_dangerous_deserialization=True,
        )

    return None


def index_uploaded_files(uploaded_files):

    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

    documents = []

    uploaded_count = 0

    for uploaded_file in uploaded_files:

        save_path = os.path.join(
            UPLOAD_FOLDER,
            uploaded_file.name,
        )

        # Skip duplicate PDFs
        if os.path.exists(save_path):
            print(f"Skipped: {uploaded_file.name}")
            continue

        with open(save_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        loader = PyPDFLoader(save_path)

        docs = loader.load()

        for page in docs:

            page.metadata["source"] = uploaded_file.name

        documents.extend(docs)

        uploaded_count += 1

    if len(documents) == 0:

        return 0

    splitter = RecursiveCharacterTextSplitter(

        chunk_size=CHUNK_SIZE,

        chunk_overlap=CHUNK_OVERLAP,

    )

    chunks = splitter.split_documents(documents)

    print(f"Created {len(chunks)} chunks")

    vectorstore = load_vectorstore()

    if vectorstore is None:

        print("Creating new FAISS index...")

        vectorstore = FAISS.from_documents(

            chunks,

            embeddings,

        )

    else:

        print("Adding new documents to existing FAISS...")

        vectorstore.add_documents(chunks)

    vectorstore.save_local(VECTORSTORE_PATH)

    print("Saved FAISS index")

    return len(chunks)