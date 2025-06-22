import os
from collections import Counter
from datetime import datetime
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import spacy
import langdetect

from transformers import pipeline

from collections import Counter
from nltk.tokenize import word_tokenize

def get_keywords(cleaned_text, top_n=10):
    """
    Extract top N frequent words from preprocessed (clean) text.
    """
    words = word_tokenize(cleaned_text.lower())
    freq_dist = Counter(words)
    keywords = [word for word, freq in freq_dist.most_common(top_n)]
    return keywords


# Load spaCy English model
import spacy
try:
    nlp = spacy.load("en_core_web_sm")
except:
    import os
    os.system("python -m spacy download en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

# Load summarization model (only once)
summarizer = pipeline("summarization", model="facebook/bart-large-cnn", framework="pt")


# Stopwords for potential future scoring use
stop_words = set(stopwords.words("english"))

# Get basic stats
def get_basic_stats(text):
    paragraphs = text.split('\n')
    num_paragraphs = len([p for p in paragraphs if p.strip() != ""])
    num_words = len(text.split())
    num_chars = len(text)
    reading_time = round(num_words / 200)  # assuming 200 WPM
    return num_paragraphs, num_words, num_chars, reading_time

# Named Entity Recognition
def get_named_entities(text):
    doc = nlp(text)
    ner_dict = {"GPE": [], "LOC": [], "ORG": [], "DATE": [], "CARDINAL": []}
    for ent in doc.ents:
        if ent.label_ in ner_dict:
            ner_dict[ent.label_].append(ent.text)
    for key in ner_dict:
        ner_dict[key] = list(set(ner_dict[key]))  # remove duplicates
    return ner_dict

# Dominant Entity Type
def detect_dominant_entity(named_entities):
    counts = {key: len(val) for key, val in named_entities.items()}
    if counts:
        return max(counts, key=counts.get)
    return "UNKNOWN"

# Language Detection
def detect_language(text):
    try:
        return langdetect.detect(text)
    except:
        return "UNKNOWN"

# Summary using Transformers
def get_summary(text):
    # Truncate text to 3500 chars for model token limit
    if len(text) > 3500:
        text = text[:3500]

    try:
        summary = summarizer(text, max_length=180, min_length=60, do_sample=False)[0]['summary_text']
        return [summary]
    except Exception as e:
        return ["Summary generation failed: " + str(e)]


# Combine Everything
def generate_metadata(raw_text, cleaned_text=None, filename="unknown_file.txt"):
    # Core stats
    num_paragraphs, num_words, num_chars, reading_time = get_basic_stats(raw_text)

    # Language
    lang = detect_language(raw_text)

    # NER
    entities = get_named_entities(raw_text)
    dominant_type = detect_dominant_entity(entities)

    # Summary
    summary = get_summary(raw_text)

    # Keywords (only if cleaned text provided)
    keywords = get_keywords(cleaned_text) if cleaned_text else []

    # Metadata dictionary
    metadata = {
        "Filename": filename,
        "Extracted on": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Document length": f"{num_chars} characters",
        "Word count": num_words,
        "Approx. Reading Time": f"{reading_time} min",
        "Paragraphs": num_paragraphs,
        "Detected Language": lang.upper(),
        "Dominant Entity Type": dominant_type,
        "Keywords": keywords,
        "=== Summary Sections ===": summary,
        "=== Named Entities ===": entities
    }

    return metadata

