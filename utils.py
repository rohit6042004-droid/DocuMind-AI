import os

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


def build_chat_history(messages, max_messages=6):
    history = ""

    for msg in messages[-max_messages:]:
        history += f"{msg['role'].capitalize()}: {msg['content']}\n"

    return history


def format_sources(docs):
    sources = []

    for doc in docs:
        sources.append({
            "document": doc.metadata.get("source", "Unknown"),
            "page": doc.metadata.get("page", "?")
        })

    return sources


def ensure_folder(path):
    os.makedirs(path, exist_ok=True)