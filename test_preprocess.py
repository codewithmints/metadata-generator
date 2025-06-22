from scripts.extract_text import extract_from_txt
from scripts.preprocess import preprocess_text
from scripts.metadata import generate_metadata
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

# Optional: Save output as .txt
def save_metadata_to_file(metadata, output_path="sample_docs/testfile_metadata.txt"):
    with open(output_path, "w", encoding="utf-8") as f:
        for key, value in metadata.items():
            if isinstance(value, dict):
                f.write(f"{key}:\n")
                for subkey, subval in value.items():
                    f.write(f"  {subkey}: {subval}\n")
            elif isinstance(value, list):
                f.write(f"{key}:\n")
                for item in value:
                    f.write(f"  - {item}\n")
            else:
                f.write(f"{key}: {value}\n")
            f.write("\n")
    print(f"✅ Metadata saved to {output_path}")

# Step 1: Load raw text
raw = extract_from_txt("sample_docs/testfile.txt")  # You can switch to extract_from_pdf() if needed

# Step 2: Clean raw text for keyword extraction
clean = preprocess_text(raw)

# Step 3: Print a preview of the cleaned result (optional)
print("\n🧼 CLEANED TEXT PREVIEW (for keywords only):")
print(clean[:300])  # show first 300 characters

# Step 4: Generate metadata using raw text (to preserve sentence structure for summary + NER)
metadata = generate_metadata(raw, cleaned_text=clean, filename="testfile.txt")


# Step 5: Display metadata
print("\n📋 METADATA:")
for key, value in metadata.items():
    print(f"{key}:\n{value}\n")

# Step 6: Save metadata to file
save_metadata_to_file(metadata, output_path="sample_docs/testfile_metadata.txt")