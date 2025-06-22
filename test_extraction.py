from scripts.extract_text import extract_from_pdf, extract_from_docx, extract_from_txt

print("PDF Text:")
print(extract_from_pdf("sample_docs/sample.pdf"))

print("\nDOCX Text:")
print(extract_from_docx("sample_docs/example.docx"))

print("\nTXT Text:")
print(extract_from_txt("sample_docs/testfile.txt"))
