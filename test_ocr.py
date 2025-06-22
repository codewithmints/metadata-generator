from scripts.extract_text import extract_from_pdf

pdf_path = "sample_docs/Sample_Scanned.pdf"

text = extract_from_pdf(pdf_path)

print("EXTRACTED TEXT:\n")
print(text)  # Print first 1000 characters
