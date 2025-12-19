import re
import nltk
from nltk.corpus import stopwords


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

    
    text = text.lower()

   
    text = re.sub(r"[^a-z\s]", " ", text)

   
    words = text.split()

   
    words = [w for w in words if w not in stop_words and len(w) > 2]

    return " ".join(words)
