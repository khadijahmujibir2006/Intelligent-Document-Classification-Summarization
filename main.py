from utils.text_extraction import extract_text_from_pdf
from utils.preprocessing import clean_text
from classifier import train_classifier, predict_doc
from summarizer import summarize


texts = [
    "invoice total amount due payment",
    "curriculum vitae skills education experience",
    "legal notice court law section",
    "email regarding meeting schedule"
]

labels = ["Invoice", "Resume", "Legal", "Email"]


model, vectorizer = train_classifier(texts, labels)


file_path = "sample.pdf"  
text = extract_text_from_pdf(file_path)
cleaned = clean_text(text)


doc_type = predict_doc(model, vectorizer, cleaned)
summary = summarize(text)

print("Document Type:", doc_type)
print("Summary:", summary)
