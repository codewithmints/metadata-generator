## 🧠 Smart Metadata Generator

A web-based Streamlit application that automatically extracts and summarizes metadata from uploaded `.txt`, `.pdf`, and `.docx` files. It uses modern NLP tools to provide clean summaries, keywords, language detection, and named entity recognition.

## 📌 Features

- Upload `.txt`, `.pdf`, or `.docx` files
- Automatic text extraction
- Text preprocessing & keyword extraction using NLTK
- Named Entity Recognition (NER) using spaCy
- Summarization using Hugging Face Transformers
- Language detection
- Downloadable `.txt` metadata output

## 📁 Folder Structure
```
📁 metadata-generator/
├── streamlit_app.py          # Main Streamlit app
├── requirements.txt          # All Python dependencies
├── README.md                 # Project documentation
├── sample_docs/              # Folder containing example input files
│   ├── sample.pdf
│   ├── scanned_example.pdf
│   └── testfile.txt
├── scripts/                  # Source code
│   ├── extract_text.py       # File parsing logic
│   ├── preprocess.py         # Text preprocessing
│   ├── metadata.py           # NER, summary, language detection
│   └── ocr_helper.py         # OCR-based text extraction using Tesseract
```



## ⚙️ Installation

📦 1. Clone the Repository
`git clone https://github.com/codewithmints/metadata-generator.git
cd metadata-generator`

🧪 2. Install Requirements
`pip install -r requirements.txt`

🧠 3. Download NLTK Resources (First Time Only)
`import nltk
nltk.download('punkt')
nltk.download('stopwords')`

▶️ 4. Run the App Locally
`streamlit run streamlit_app.py`


## 📝 Example Workflow

1. Upload any .pdf, .docx, or .txt file

2. View extracted metadata including:
- Filename
- Language
- Summary
- Keywords
- Named Entities

3. Optionally download a .txt metadata report

## 📚 Built With
- Streamlit
- spaCy
- Transformers
- NLTK
- pdfplumber
- PyMuPDF
- python-docx

## 👤 Author
Meet Jain
GitHub: @codewithmints

