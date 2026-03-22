def chunk_text(text, max_chunk_size=400):
    paragraphs = text.split("\n\n")
    
    chunks = []
    current_chunk = ""

    for para in paragraphs:
        para = para.strip()
        if not para:
            continue

        # If paragraph itself is too big → split it
        if len(para) > max_chunk_size:
            for i in range(0, len(para), max_chunk_size):
                chunks.append(para[i:i+max_chunk_size])
            continue

        # Normal merging
        if len(current_chunk) + len(para) < max_chunk_size:
            current_chunk += para + "\n\n"
        else:
            if current_chunk:
                chunks.append(current_chunk.strip())
            current_chunk = para + "\n\n"

    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks