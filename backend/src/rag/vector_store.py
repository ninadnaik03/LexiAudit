import chromadb
from sentence_transformers import SentenceTransformer

# ✅ Persistent DB
client = chromadb.Client(
    settings=chromadb.Settings(
        persist_directory="chroma_db"
    )
)

collection = client.get_or_create_collection(name="legal_docs")

model = SentenceTransformer("all-MiniLM-L6-v2")


def store_chunks(chunks):
    embeddings = model.encode(chunks)

    ids = [str(i) for i in range(len(chunks))]

    collection.upsert(
        documents=chunks,
        embeddings=embeddings.tolist(),
        ids=ids
    )


def query_chunks(query):
    query_embedding = model.encode([query]).tolist()

    results = collection.query(
        query_embeddings=query_embedding,
        n_results=10
    )

    docs = results.get("documents", [[]])[0]

    if not docs:
        return {"documents": [[]]}

    # 🔥 KEYWORD BOOST
    keywords = [
        "acquisition agreement",
        "entered into",
        "by and among",
        "this agreement",
        "agreement is entered"
    ]

    def score(doc):
        doc_lower = doc.lower()
        score = 0

        for k in keywords:
            if k in doc_lower:
                score += 2

        score += max(0, 5 - docs.index(doc))  # bias to early chunks

        return score

    docs = sorted(docs, key=score, reverse=True)

    return {"documents": [docs]}