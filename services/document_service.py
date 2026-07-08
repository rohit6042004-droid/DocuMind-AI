import os
import shutil

from config import UPLOAD_FOLDER


def get_uploaded_documents():
    if not os.path.exists(UPLOAD_FOLDER):
        return []

    return sorted(os.listdir(UPLOAD_FOLDER))


def clear_documents():
    if os.path.exists(UPLOAD_FOLDER):
        shutil.rmtree(UPLOAD_FOLDER)

    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    def clear_documents():
    import os
    import shutil
    from config import UPLOAD_FOLDER

    if os.path.exists(UPLOAD_FOLDER):
        shutil.rmtree(UPLOAD_FOLDER)

    os.makedirs(UPLOAD_FOLDER, exist_ok=True)