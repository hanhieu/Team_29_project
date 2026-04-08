from rag.vectorstore import get_collection


def retrieve(query: str, user_type: str, top_k: int = 3) -> list[dict]:
    collection = get_collection()
    results = collection.query(
        query_texts=[query],
        n_results=top_k,
        where={"user_type": user_type},
    )

    chunks = []
    if results and results["metadatas"]:
        for meta, distance in zip(results["metadatas"][0], results["distances"][0]):
            chunks.append({
                "question": meta.get("question", ""),
                "answer": meta.get("answer", ""),
                "score": distance,
            })
    return chunks
