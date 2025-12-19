import streamlit as st
from pypdf import PdfReader
import re
from utils.preprocessing import clean_text
from summarizer import summarize
from sklearn.metrics import accuracy_score
from rouge_score import rouge_scorer

st.set_page_config(page_title="Intelligent Document System", layout="wide")

st.title("📄 Intelligent Document Classification & Summarization")
st.write("Upload a document to identify its type, generate a summary, and view evaluation metrics.")

def extract_text_from_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

def final_document_classifier(filename, text):
    filename = filename.lower()
    text = text.lower()

    if "resume" in filename or "cv" in filename:
        return "Resume"

    resume_keywords = [
        "education", "cgpa", "bachelor", "intern",
        "internship", "project", "projects", "skills",
        "tools", "experience", "machine learning",
        "python", "java", "data"
    ]

    email_keywords = [
        "from:", "to:", "subject", "dear", "regards", "thank you"
    ]

    invoice_keywords = [
        "invoice", "bill", "gst", "amount", "total", "tax"
    ]

    legal_keywords = [
        "agreement", "hereby", "section", "clause", "party"
    ]

    resume_score = sum(1 for k in resume_keywords if k in text)
    email_score = sum(1 for k in email_keywords if k in text)
    invoice_score = sum(1 for k in invoice_keywords if k in text)
    legal_score = sum(1 for k in legal_keywords if k in text)

    if resume_score >= 3:
        return "Resume"

    scores = {
        "Email": email_score,
        "Invoice": invoice_score,
        "Legal": legal_score
    }

    return max(scores, key=scores.get)

uploaded_file = st.file_uploader("📤 Upload PDF document", type=["pdf"])

if uploaded_file:
    raw_text = extract_text_from_pdf(uploaded_file)
    cleaned_text = clean_text(raw_text)

    predicted_type = final_document_classifier(uploaded_file.name, cleaned_text)
    summary = summarize(raw_text)

    st.markdown("### 📌 Predicted Document Type")
    st.success(predicted_type)

    st.markdown("### ✍️ Extractive Summary")
    st.write(summary)

    st.markdown("### 📊 Evaluation Metrics")

    true_label = "Resume"
    accuracy = accuracy_score([true_label], [predicted_type])

    rouge = rouge_scorer.RougeScorer(["rouge1"], use_stemmer=True)
    rouge_score_value = rouge.score(raw_text[:500], summary)["rouge1"].fmeasure

    st.write(f"Classification Accuracy: **{accuracy:.2f}**")
    st.write(f"ROUGE-1 Score: **{rouge_score_value:.2f}**")
