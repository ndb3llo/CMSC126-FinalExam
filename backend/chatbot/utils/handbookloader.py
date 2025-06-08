import os
import re
from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TXT_PATH = os.path.join(BASE_DIR, "FAQUP-OUTPUT.txt")

CHUNK_SIZE = 800  # You can adjust this for your AI context size


def load_handbook():
    with open(TXT_PATH, "r", encoding="utf-8") as f:
        return f.read()

def generate_chunks_with_embeddings():
    chunked_sections = generate_chunks()
    texts = [chunk["content"] for chunk in chunked_sections]
    embeddings = model.encode(texts, convert_to_numpy=True)
    return chunked_sections, embeddings

def split_into_chapters_sections_and_subsections(full_text):
    chapter_pattern = re.compile(r'(?m)^Chapter\s+(?P<chapter>[IVXLCDM]+)\.\s+(?P<title>.+)$')
    section_pattern = re.compile(r'(?m)^Section\s+\d+\.\s+.*')
    subsection_pattern = re.compile(r'(?m)^[a-z]\.\s+.*')

    chapters = []
    chapter_matches = list(chapter_pattern.finditer(full_text))
    
    for i, chapter_match in enumerate(chapter_matches):
        chap_start = chapter_match.end()
        chap_end = chapter_matches[i + 1].start() if i + 1 < len(chapter_matches) else len(full_text)

        chapter_title = f"Chapter {chapter_match.group('chapter')}: {chapter_match.group('title').strip()}"
        chapter_content = full_text[chap_start:chap_end].strip()

        section_matches = list(section_pattern.finditer(chapter_content))
        sections = []

        for j, section_match in enumerate(section_matches):
            sec_start = section_match.end()
            sec_end = section_matches[j + 1].start() if j + 1 < len(section_matches) else len(chapter_content)

            section_title = section_match.group().strip()
            section_body = chapter_content[sec_start:sec_end].strip()

            subsection_matches = list(subsection_pattern.finditer(section_body))
            subsections = []

            if subsection_matches:
                for k, sub_match in enumerate(subsection_matches):
                    sub_start = sub_match.end()
                    sub_end = subsection_matches[k + 1].start() if k + 1 < len(subsection_matches) else len(section_body)

                    sub_title = sub_match.group().strip()
                    sub_body = section_body[sub_start:sub_end].strip()
                    subsections.append((sub_title, sub_body))
            else:
                subsections.append((section_title, section_body))

            sections.append({
                "section_title": section_title,
                "subsections": subsections
            })

        chapters.append({
            "chapter_title": chapter_title,
            "sections": sections
        })

    return chapters


def chunk_text(text, chunk_size=CHUNK_SIZE):
    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]


def generate_chunks():
    full_text = load_handbook()
    chapters = split_into_chapters_sections_and_subsections(full_text)

    chunked_sections = []
    for chap in chapters:
        for sec in chap["sections"]:
            for sub_index, (sub_title, sub_body) in enumerate(sec["subsections"]):
                chunks = chunk_text(sub_body)
                for i, chunk in enumerate(chunks):
                    chunked_sections.append({
                        "chapter": chap["chapter_title"],
                        "section": sec["section_title"],
                        "subsection": sub_title,
                        "chunk_index": i,
                        "content": chunk
                    })

    return chunked_sections

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def find_relevant_chunks(query, chunked_sections, chunk_embeddings, top_k=3):
    query_embedding = model.encode([query], convert_to_numpy=True)[0]
    similarities = []
    for idx, emb in enumerate(chunk_embeddings):
        sim = cosine_similarity(query_embedding, emb)
        similarities.append((sim, chunked_sections[idx]))
    similarities.sort(key=lambda x: x[0], reverse=True)
    return [item[1] for item in similarities[:top_k]]
