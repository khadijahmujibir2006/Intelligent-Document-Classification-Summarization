from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

def train_classifier(texts, labels):
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(texts)

    model = LogisticRegression()
    model.fit(X, labels)

    return model, vectorizer

def predict_doc(model, vectorizer, text):
    X = vectorizer.transform([text])
    return model.predict(X)[0]
