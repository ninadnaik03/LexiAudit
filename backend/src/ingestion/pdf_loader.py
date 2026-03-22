import pdfplumber
import os
import hashlib
import shutil

from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

from src.utils.chunker import chunk_text
from src.utils.layout_parser import extract_sections
from src.rag.vector_store import store_chunks, query_chunks
from src.rag.rag_pipeline import rag_query
from src.utils.party_extractor import extract_parties
from src.ner.ner_engine import extract_entities
from src.analyzer.anomaly_detector import detect_anomalies
from src.analyzer.contract_classifier import classify_contract

app = FastAPI()

# 🌐 CORS (required for frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def extract_text_from_pdf(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted + "\n"
    return text


def get_file_hash(file_path):
    with open(file_path, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()


# 🚀 API ENDPOINT (SAFE ADDITION)
@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):

    file_path = f"temp_{file.filename}"

    # Save uploaded file
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:
        text = extract_text_from_pdf(file_path)

        # Layout parsing
        sections = extract_sections(text)

        # Chunking
        chunks = chunk_text(text, max_chunk_size=400)

        # ✅ SMART CACHE (PRESERVED)
        hash_file = "db_hash.txt"
        current_hash = get_file_hash(file_path)

        rebuild_db = True

        if os.path.exists(hash_file):
            with open(hash_file, "r") as f:
                old_hash = f.read().strip()
                if old_hash == current_hash:
                    rebuild_db = False

        if rebuild_db:
            store_chunks(chunks)
            with open(hash_file, "w") as f:
                f.write(current_hash)

        # Core analysis
        contract_type = classify_contract(text)
        parties = extract_parties(text)
        entities = extract_entities(text[:3000])
        report = detect_anomalies(text, contract_type)

        return {
            "contract_type": contract_type,
            "parties": parties,
            "entities": entities,
            "risks": report["risks"]["HIGH"] + report["risks"]["MEDIUM"],
        }

    finally:
        if os.path.exists(file_path):
            os.remove(file_path)


# 🧪 KEEP YOUR ORIGINAL TEST MODE (UNCHANGED)
if __name__ == "__main__":
    sample_path = "data/sample.pdf"
    
    print("\n📄 Extracting text from PDF...")
    text = extract_text_from_pdf(sample_path)

    print("\n🧩 Layout-Aware Section Parsing...\n")
    sections = extract_sections(text)

    for sec in sections[:5]:
        print(f"📌 {sec['title']}")
        print(sec["content"][:150])
        print("\n---\n")

    print("🔪 Chunking text...")
    chunks = chunk_text(text, max_chunk_size=400)
    print(f"\nTotal chunks: {len(chunks)}")

    hash_file = "db_hash.txt"
    current_hash = get_file_hash(sample_path)

    rebuild_db = True

    if os.path.exists(hash_file):
        with open(hash_file, "r") as f:
            old_hash = f.read().strip()
            if old_hash == current_hash:
                rebuild_db = False

    if rebuild_db:
        print("\n💾 Rebuilding vector DB...")
        store_chunks(chunks)

        with open(hash_file, "w") as f:
            f.write(current_hash)

        print("✅ Vector DB updated")
    else:
        print("\n⚡ Using existing vector DB (up-to-date)")

    print("\n📊 Contract Classification...\n")
    contract_type = classify_contract(text)
    print("Detected Contract Type:", contract_type)

    print("\n⚖️ Extracting parties...\n")
    parties = extract_parties(text)

    if parties:
        for p in parties:
            print("-", p)
    else:
        print("No parties found.")

    print("\n🧠 NER Extraction...\n")
    entities = extract_entities(text[:3000])

    for key, values in entities.items():
        print(f"{key}:")
        for v in values:
            print(" -", v)
        print()

    print("\n🚨 Anomaly Detection...\n")
    report = detect_anomalies(text, contract_type)

    print("Missing Clauses:")
    for c in report["missing_clauses"]:
        print(" -", c)

    print("\n🔴 HIGH RISK TERMS:")
    for r in report["risks"]["HIGH"]:
        print(" -", r)

    print("\n🟡 MEDIUM RISK TERMS:")
    for r in report["risks"]["MEDIUM"]:
        print(" -", r)

    query = "entered into by and among agreement parties companies"

    print("\n🔎 Retrieving relevant chunks...")
    results = query_chunks(query)

    print("\n--- Top Retrieved Chunks ---\n")
    if results and "documents" in results and results["documents"]:
        for doc in results['documents'][0][:3]:
            print(doc[:300])
            print("\n---\n")
    else:
        print("No relevant chunks found.")

    print("\n🤖 Generating Answer...\n")
    answer = rag_query(query, parties)

    print("=== FINAL ANSWER ===\n")
    print(answer)