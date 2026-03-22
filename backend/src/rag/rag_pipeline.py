from src.rag.llm_engine import query_llm


def rag_query(user_query, parties=None):
    """
    Smart RAG Pipeline:
    - ⚡ Uses structured data when available (fast, no LLM)
    - 🤖 Falls back to LLM only if needed
    """

    query_lower = user_query.lower()

    # 🔥 FAST PATH (no LLM needed)
    if parties and len(parties) > 0:
        if any(keyword in query_lower for keyword in ["party", "parties", "who"]):
            return "The parties involved in the agreement are:\n" + "\n".join(
                f"- {p}" for p in parties
            )

    # 🤖 FALLBACK (LLM only when required)
    context = "\n".join(parties) if parties else "No structured data available."

    prompt = f"""
You are a legal assistant.

Answer the user's question based on the given context.

Context:
{context}

Question:
{user_query}

Answer:
"""

    return query_llm(prompt)