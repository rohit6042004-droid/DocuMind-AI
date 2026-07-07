import os

from config import UPLOAD_FOLDER


def get_uploaded_documents():

    if not os.path.exists(UPLOAD_FOLDER):

        return []

    return sorted(os.listdir(UPLOAD_FOLDER))


def delete_document(filename):

    path = os.path.join(

        UPLOAD_FOLDER,

        filename,

    )

    if os.path.exists(path):

        os.remove(path)

        return True

    return False