import streamlit as st
import os
import io
from datetime import datetime

from scripts.extract_text import extract_from_txt, extract_from_pdf, extract_from_docx
from scripts.preprocess import preprocess_text
from scripts.metadata import generate_metadata

st.set_page_config(page_title="Smart Metadata Generator", layout="wide")
st.title("🧠 Smart Metadata Generator")

st.markdown("Upload a `.txt`, `.pdf`, or `.docx` file to automatically extract summary, keywords, and metadata.")

uploaded_file = st.file_uploader("📎 Upload file", type=["txt", "pdf", "docx"])

if uploaded_file is not None:
    try:
        # Save file to local dir
        filepath = os.path.join("sample_docs", uploaded_file.name)
        with open(filepath, "wb") as f:
            f.write(uploaded_file.read())
        st.success(f"✅ File uploaded: {uploaded_file.name}")

        # Extract raw text
        st.info("📄 Extracting text...")
        if uploaded_file.name.endswith(".txt"):
            raw_text = extract_from_txt(filepath)
        elif uploaded_file.name.endswith(".pdf"):
            raw_text = extract_from_pdf(filepath)
        elif uploaded_file.name.endswith(".docx"):
            raw_text = extract_from_docx(filepath)
        else:
            st.error("Unsupported file type.")
            st.stop()

        st.code(raw_text[:1000], language="text")  # Preview

        # Preprocess
        st.info("🧼 Preprocessing text...")
        clean_text = preprocess_text(raw_text)

        # Generate Metadata
        st.info("🧠 Generating metadata...")
        metadata = generate_metadata(
            raw_text=raw_text,
            cleaned_text=clean_text,
            filename=uploaded_file.name
        )

        # Display Metadata
        st.subheader("📋 Metadata Output")
        for key, value in metadata.items():
            if isinstance(value, dict):
                st.markdown(f"**{key}:**")
                for subkey, subval in value.items():
                    st.markdown(f"- {subkey}: {subval}")
            elif isinstance(value, list):
                st.markdown(f"**{key}:**")
                for item in value:
                    st.markdown(f"- {item}")
            else:
                st.markdown(f"**{key}:** {value}")

        # Prepare Download
        metadata_text = io.StringIO()
        for key, value in metadata.items():
            metadata_text.write(f"{key}:\n")
            if isinstance(value, list):
                for v in value:
                    metadata_text.write(f"  - {v}\n")
            elif isinstance(value, dict):
                for subkey, subval in value.items():
                    metadata_text.write(f"  {subkey}: {subval}\n")
            else:
                metadata_text.write(f"{value}\n")
            metadata_text.write("\n")

        # Download button
        st.download_button(
            label="📥 Download Metadata as TXT",
            data=metadata_text.getvalue(),
            file_name=f"{uploaded_file.name}_metadata.txt",
            mime="text/plain"
        )

    except Exception as e:
        st.error(f"❌ Error occurred: {e}")
