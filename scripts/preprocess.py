import nltk
nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Load stopwords
stop_words = set(stopwords.words('english'))

def clean_for_keywords(text):
    """
    For keyword extraction: remove punctuation, numbers, stopwords.
    """
    tokens = word_tokenize(text)
    words = [
        w.lower() for w in tokens
        if w.isalpha() and w.lower() not in stop_words
    ]
    return ' '.join(words)

def preprocess_text(text):
    """
    Main wrapper (optional): for backward compatibility.
    """
    return clean_for_keywords(text)

