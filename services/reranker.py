from sentence_transformers import CrossEncoder

print("✅ RERANKER FILE LOADED")

RERANKER_MODEL = "cross-encoder/ms-marco-MiniLM-L-6-v2"

reranker = CrossEncoder(RERANKER_MODEL)


def rerank_documents(question, docs, top_n=4):
    if not docs:
        return []

    pairs = [[question, doc.page_content] for doc in docs]

    scores = reranker.predict(pairs)

    print("\n========== CROSS ENCODER SCORES ==========")

    scored_docs = []

    for doc, score in zip(docs, scores):
        print(
            f"{score:.4f} | "
            f"{doc.metadata.get('source')} | "
            f"Page {doc.metadata.get('page')}"
        )

        scored_docs.append((doc, score))

    scored_docs.sort(
        key=lambda x: x[1],
        reverse=True
    )

    print("\n========== AFTER SORT ==========")

    for doc, score in scored_docs:
        print(
            f"{score:.4f} | "
            f"{doc.metadata.get('source')} | "
            f"Page {doc.metadata.get('page')}"
        )

    return [doc for doc, score in scored_docs[:top_n]]