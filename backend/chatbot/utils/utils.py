import PyPDF2

def extract_handbook_text(pdf_path, txt_path):
    text = ""
    with open(pdf_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    with open(txt_path, "w", encoding="utf-8") as out:
        out.write(text)
