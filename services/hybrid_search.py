import re
from rank_bm25 import BM25Okapi


def tokenize(text):
    return re.findall(r"\w+", text.lower())


def hybrid_search(question, vectorstore, selected_document="All Documents", k=30):
    # 1. FAISS semantic search
    faiss_docs = vectorstore.similarity_search(question, k=k)

    # Optional document filtering
    if selected_document != "All Documents":
        faiss_docs = [
            doc for doc in faiss_docs
            if doc.metadata.get("source") == selected_document
        ]

    if not faiss_docs:
        return []

    # 2. BM25 keyword ranking on FAISS candidate docs
    tokenized_docs = [tokenize(doc.page_content) for doc in faiss_docs]
    bm25 = BM25Okapi(tokenized_docs)

    scores = bm25.get_scores(tokenize(question))

    scored_docs = list(zip(faiss_docs, scores))

    scored_docs.sort(
        key=lambda x: x[1],
        reverse=True
    )

    # 3. Return BM25-ranked candidates
    return [doc for doc, score in scored_docs[:k]]