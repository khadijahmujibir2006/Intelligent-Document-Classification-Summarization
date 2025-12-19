import re
import nltk
from nltk.corpus import stopwords

# Download stopwords if not already available
try:
    stop_words = set(stopwords.words("english"))
except LookupError:
    nltk.download("stopwords")
    stop_words = set(stopwords.words("english"))


def clean_text(text: str) -> str:
    """
    Cleans extracted document text for classification.
    - Lowercases text
    - Removes numbers and special characters
    - Removes stopwords
    - Removes very short tokens
    """

    if not text:
        return ""

    # Convert to lowercase
    text = text.lower()

    # Remove numbers and special characters (keep letters & spaces)
    text = re.sub(r"[^a-z\s]", " ", text)

    # Tokenize
    words = text.split()

    # Remove stopwords and short words
    words = [w for w in words if w not in stop_words and len(w) > 2]

    return " ".join(words)
