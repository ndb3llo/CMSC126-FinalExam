import re
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_FILE = os.path.join(BASE_DIR, "FAQUP-RAW.txt")
OUTPUT_FILE = os.path.join(BASE_DIR, "FAQUP-OUTPUT.txt")


def clean_bullets(text):
    # Normalize different bullet styles into •
    text = re.sub(r"(?m)^[-•*]\s+", "• ", text)
    # Keep bullet indentation intact
    text = re.sub(r"(?m)^(\s*)•", r"\1•", text)
    return text


def format_chapters_sections(text):
    # Fix Chapter headers: "I. TITLE" -> "\nChapter I. TITLE"
    text = re.sub(r"(?m)^\s*([IVXLCDM]+)\.\s+([A-Z][^\n]{3,})", r"\nChapter \1. \2", text)

    # Fix Section headers: "Section 1. Title" -> "\nSection 1. Title"
    text = re.sub(r"(?m)^\s*Section\s+\d+\.\s+.*", lambda m: "\n" + m.group(0).strip(), text)

    # Fix Subsections: "a. Title" -> "\na. Title"
    text = re.sub(r"(?m)^([a-z])\.\s+([^\n]+)", r"\n\1. \2", text)

    return text


def normalize_whitespace(text):
    # Remove trailing spaces
    text = re.sub(r"[ \t]+$", "", text, flags=re.MULTILINE)
    # Normalize multiple newlines
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def format_handbook(input_path, output_path):
    with open(input_path, "r", encoding="utf-8") as f:
        raw_text = f.read()

    text = raw_text
    text = clean_bullets(text)
    text = format_chapters_sections(text)
    text = normalize_whitespace(text)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)

    print(f"Formatted handbook saved to {output_path}")


if __name__ == "__main__":
    format_handbook(INPUT_FILE, OUTPUT_FILE)
