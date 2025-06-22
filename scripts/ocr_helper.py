import fitz                              # PyMuPDF
from PIL import Image
import pytesseract
import io

# Point to your Tesseract binary (leave exactly as below if path is correct)
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\meetj\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

def ocr_extract_text_from_pdf(pdf_path):
    print("🔧 OCR fallback: rendering pages with PyMuPDF …")
    text = ""

    with fitz.open(pdf_path) as doc:
        for idx, page in enumerate(doc):
            print(f"🔍  OCR on page {idx + 1}")
            pix = page.get_pixmap(dpi=300)                     # render page
            img = Image.open(io.BytesIO(pix.tobytes("png")))   # to PIL image
            text += pytesseract.image_to_string(img)

    return text

