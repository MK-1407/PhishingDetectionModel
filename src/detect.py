import joblib
from scipy.sparse import hstack

model = joblib.load("model/logistic_model1.pkl")
vectorizer = joblib.load("model/tfidf_vectorizer.pkl")


def detect_mail(text: str, url: int):
    X_test_text = vectorizer.transform([text])
    X_test_url = [[url]]

    X_test = hstack([X_test_text, X_test_url])

    prediction = model.predict(X_test)
    probability = model.predict_proba(X_test)

    if prediction[0] == 1:
        confidence = probability[0][1] * 100
        print(f"Phishing Email ({confidence:.2f}% confidence)")
    else:
        confidence = probability[0][0] * 100
        print(f"Safe Email ({confidence:.2f}% confidence)")