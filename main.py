from utils.text_extraction import extract_text_from_pdf
from utils.preprocessing import clean_text
from classifier import train_classifier, predict_doc
from summarizer import summarize

# Sample training data
texts = [
    "invoice total amount due payment",
    "curriculum vitae skills education experience",
    "legal notice court law section",
    "email regarding meeting schedule"
]

labels = ["Invoice", "Resume", "Legal", "Email"]

# Train model
model, vectorizer = train_classifier(texts, labels)

# Input document
file_path = "sample.pdf"   # replace with your pdf file
text = extract_text_from_pdf(file_path)
cleaned = clean_text(text)

# Prediction
doc_type = predict_doc(model, vectorizer, cleaned)
summary = summarize(text)

print("Document Type:", doc_type)
print("Summary:", summary)
