import difflib
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TXT_PATH = os.path.join(BASE_DIR, "Student-Handbook-2022.txt")

def load_and_chunk_handbook(chunk_size=1000):
    with open(TXT_PATH, "r", encoding="utf-8") as f:
        full_text = f.read()
    print(f"Loaded handbook text length: {len(full_text)} characters")
    print("First 200 chars:", full_text[:200])
    print("Last 200 chars:", full_text[-200:])

    chunks = []
    for i in range(0, len(full_text), chunk_size):
        chunks.append(full_text[i:i+chunk_size])
    print(f"Total chunks: {len(chunks)}")
    print(f"Last chunk size: {len(chunks[-1])}")

    return chunks

def find_relevant_chunks(query, chunks, top_k=3):
    return sorted(
        chunks,
        key=lambda chunk: difflib.SequenceMatcher(None, query.lower(), chunk.lower()).ratio(),
        reverse=True
    )[:top_k]

def split_into_sections(full_text):
    sections = full_text.split("Section")
    result = []
    for sec in sections:
        if sec.strip():
            lines = sec.strip().split('\n', 1)
            title = lines[0].strip() if lines else "Untitled"
            content = lines[1].strip() if len(lines) > 1 else ""
            result.append((title, content))
    return result