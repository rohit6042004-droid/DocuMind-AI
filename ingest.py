import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings

from config import DATA_FOLDER, VECTORSTORE_PATH, EMBEDDING_MODEL, CHUNK_SIZE, CHUNK_OVERLAP

documents = []

pdf_files = [file for file in os.listdir(DATA_FOLDER) if file.endswith(".pdf")]

if not pdf_files:
    raise ValueError("No PDF files found in the data folder.")

for file in pdf_files:
    print(f"Reading: {file}")
    path = os.path.join(DATA_FOLDER, file)

    loader = PyPDFLoader(path)
    docs = loader.load()

    for doc in docs:
        doc.metadata["source"] = file

    documents.extend(docs)

print(f"Loaded {len(documents)} pages.")

splitter = RecursiveCharacterTextSplitter(
    chunk_size=CHUNK_SIZE,
    chunk_overlap=CHUNK_OVERLAP,
    separators=["\n\n", "\n", ". ", " "]
)

chunks = splitter.split_documents(documents)

print(f"Created {len(chunks)} chunks.")

embeddings = OllamaEmbeddings(model=EMBEDDING_MODEL)

vectorstore = FAISS.from_documents(chunks, embeddings)

vectorstore.save_local(VECTORSTORE_PATH)

print("✅ Vector database created successfully!")