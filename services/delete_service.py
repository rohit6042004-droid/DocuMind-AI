import os
import shutil

from config import UPLOAD_FOLDER


# Add more vector/index folders here if your project uses a different name.
POSSIBLE_INDEX_FOLDERS = [
    "faiss_index",
    "vectorstore",
    "vector_store",
    "db",
    "storage",
]


def clear_documents():
    """
    Remove all uploaded PDFs and common local vector index folders.
    """
    if os.path.exists(UPLOAD_FOLDER):
        shutil.rmtree(UPLOAD_FOLDER)

    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

    for folder in POSSIBLE_INDEX_FOLDERS:
        if os.path.exists(folder):
            shutil.rmtree(folder)
