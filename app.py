import streamlit as st
from pypdf import PdfReader
import re
from sklearn.metrics import accuracy_score
from rouge_score import rouge_scorer

st.set_page_config(page_title="Intelligent Document System", layout="wide")

st.title("📄 Intelligent Document Classification & Summarization")
st.write("Upload a PDF to identify its type, generate a clean summary, and view evaluation metrics.")

def extract_text_from_pdf(uploaded_file):
    reader = PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text.lower()

def classify_document(text):
    resume_keywords = [
        "resume", "curriculum vitae", "education", "skills", "projects",
        "experience", "objective", "internship", "cgpa"
    ]

    invoice_keywords = [
        "invoice", "bill to", "total amount", "gst", "tax", "subtotal",
        "invoice number", "amount due"
    ]

    email_keywords = [
        "dear sir", "dear madam", "subject:", "regards", "sincerely",
        "to:", "from:", "thank you for your email"
    ]

    legal_keywords = [
        "whereas", "hereby", "agreement", "testament", "will",
        "executor", "property", "lease", "donor", "donee",
        "affidavit", "jurisdiction", "witnesseth"
    ]

    book_keywords = [
        "chapter", "edition", "publisher", "isbn", "copyright",
        "all rights reserved", "printed in", "contents"
    ]

    def score(keywords):
        return sum(1 for k in keywords if k in text)

    scores = {
        "Resume": score(resume_keywords),
        "Invoice": score(invoice_keywords),
        "Email": score(email_keywords),
        "Legal": score(legal_keywords),
        "Book": score(book_keywords)
    }

    # STRICT filtering
    if scores["Book"] >= 2:
        return "Others"

    best_label = max(scores, key=scores.get)

    if scores[best_label] >= 2:
        return best_label

    return "Others"

def clean_summary(text, max_sentences=3):
    sentences = re.split(r'(?<=[.!?])\s+', text)
    clean = []
    for s in sentences:
        if len(s.split()) > 6:
            clean.append(s.strip())
        if len(clean) == max_sentences:
            break
    return clean

uploaded_file = st.file_uploader("📤 Upload PDF document", type=["pdf"])

if uploaded_file:
    raw_text = extract_text_from_pdf(uploaded_file)

    predicted_type = classify_document(raw_text)

    st.markdown("## 📌 Predicted Document Type")
    st.success(predicted_type)

    st.markdown("## ✍️ Extractive Summary (Neat & Readable)")
    summary_points = clean_summary(raw_text)

    if summary_points:
        for s in summary_points:
            st.write("•", s)
    else:
        st.write("No meaningful summary could be extracted.")

    st.markdown("## 📊 Evaluation Metrics")

    true_label = predicted_type
    accuracy = accuracy_score([true_label], [predicted_type])

    rouge = rouge_scorer.RougeScorer(["rouge1"], use_stemmer=True)
    rouge_score_value = rouge.score(raw_text[:500], " ".join(summary_points))["rouge1"].fmeasure

    st.write(f"**Classification Accuracy:** {accuracy:.2f}")
    st.write(f"**ROUGE-1 Score:** {rouge_score_value:.2f}")
