from sentence_transformers import CrossEncoder


RERANKER_MODEL = "cross-encoder/ms-marco-MiniLM-L-6-v2"

reranker = CrossEncoder(RERANKER_MODEL)


def rerank_documents(question, docs, top_n=4):
    if not docs:
        return []

    pairs = []

    for doc in docs:
        pairs.append([question, doc.page_content])

    scores = reranker.predict(pairs)

    scored_docs = list(zip(docs, scores))

    scored_docs = sorted(
        scored_docs,
        key=lambda x: x[1],
        reverse=True
    )

    reranked_docs = [doc for doc, score in scored_docs[:top_n]]

    return reranked_docs