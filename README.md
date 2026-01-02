📄 Intelligent Document Classification & Summarization

An NLP-based system that automatically classifies unstructured documents and generates concise summaries, with evaluation metrics displayed through a simple interactive UI.

🔍 Problem Statement

Organizations deal with large volumes of unstructured documents such as resumes, invoices, legal notices, and emails.
Manual sorting and understanding of these documents is inefficient and error-prone.

This project aims to automate:

Document type identification

Content summarization

Performance evaluation

🎯 Objectives

Classify documents into Resume / Invoice / Legal / Email

Generate an extractive summary of the document

Display classification accuracy

Evaluate summarization using ROUGE score

Provide a simple UI for document upload and result visualization

🛠️ Technologies Used

Python

Natural Language Processing (NLP)

Streamlit – User Interface

PyPDF – PDF text extraction

NLTK – Text preprocessing

Scikit-learn – Accuracy metric

ROUGE Score – Summary evaluation

🧠 System Architecture

Upload PDF document

Extract text from PDF

Preprocess text (cleaning & normalization)

Classify document type

Generate extractive summary

Evaluate using accuracy & ROUGE score

Display results in UI

📂 Project Structure
Intelligent-Document-Classification-Summarization/
│
├── app.py                  # Streamlit application
├── classifier.py           # Document classification logic
├── summarizer.py           # Extractive summarization
├── utils/
│   └── preprocessing.py    # Text cleaning functions
├── requirements.txt        # Project dependencies
├── README.md               # Project documentation

🧾 Document Classification

The system classifies documents into:

Resume

Email

Invoice

Legal

Resume Detection (Extra Credit)

A strong hybrid logic is used:

Filename-based detection (e.g., “resume”, “cv”)

Keyword-based detection (education, skills, internships)

Structural patterns from text

This approach ensures robust classification even for noisy or designed PDFs.

✍️ Summarization

Uses Extractive Summarization

Selects key sentences directly from the document

Maintains original context and meaning

Suitable for resumes, emails, and formal documents

📊 Evaluation Metrics
Classification Accuracy

Measures correctness of predicted document type

Displayed for demonstration

Meaningful when evaluated on multiple documents

ROUGE Score

ROUGE-1 score used

Evaluates quality of generated summary

Higher score indicates better relevance

🖥️ User Interface

Built using Streamlit

Features:

PDF upload (drag & drop)

Predicted document type

Extractive summary

Accuracy & ROUGE score

Runs locally on browser

✅ Expected Outcomes Achieved

✔ Document type classification
✔ Extractive document summary
✔ Accuracy score for classification
✔ ROUGE score for summarization
✔ Simple and interactive UI

⚠️ Limitations

Accuracy depends on document variety

Extractive summaries may miss deeper context

OCR not included for scanned PDFs

🚀 Future Enhancements

Abstractive summarization (T5 / BART)

OCR support for scanned documents

Batch document upload

Machine learning model integration

Cloud deployment

🎓 Conclusion

This project successfully demonstrates an intelligent NLP-based system capable of classifying documents, generating summaries, and evaluating performance through standard metrics, fulfilling all expected outcomes.

👩‍💻 Author

Khadijah Mujibir Rahman
B.E. Computer Science and Engineering
St. Joseph’s Institute of Technology

⭐ How to Run
pip install -r requirements.txt
streamlit run app.py

