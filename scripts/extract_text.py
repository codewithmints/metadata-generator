import pdfplumber
from docx import Document
from scripts.ocr_helper import ocr_extract_text_from_pdf

def extract_from_pdf(file_path):
    try:
        text = ""
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text

        # If no text is found, fall back to OCR
        if text.strip() == "":
            print("📉 No text found with pdfplumber.")
            print("⚙️ Falling back to Tesseract OCR...")
            text = ocr_extract_text_from_pdf(file_path)

        return text

    except Exception as e:
        print("❌ Error in extract_from_pdf:", e)
        print("⚙️ Falling back to OCR anyway...")
        return ocr_extract_text_from_pdf(file_path)

def extract_from_docx(file_path):
    doc = Document(file_path)
    return '\n'.join([p.text for p in doc.paragraphs])

def extract_from_txt(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

