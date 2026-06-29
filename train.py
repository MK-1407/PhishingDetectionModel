import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from scipy.sparse import hstack
import joblib

dataset = "C:\\Users\\mayan\\.cache\\kagglehub\\datasets\\naserabdullahalam\\phishing-email-dataset\\versions\\1"

df = pd.read_csv("datasets\\merged_dataset.csv")
X = df[["text", "urls"]]
y = df["label"]
print(df.iloc[0]["text"])
print(df.iloc[0]["label"])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
vectorizer = TfidfVectorizer()

X_train_text = vectorizer.fit_transform(X_train["text"])
X_test_text = vectorizer.transform(X_test["text"])
X_train_url = X_train[["urls"]]
X_test_url = X_test[["urls"]]
X_train = hstack([X_train_text, X_train_url])
X_test = hstack([X_test_text, X_test_url])

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
joblib.dump(model, "model/logistic_model1.pkl")
joblib.dump(vectorizer, "model/tfidf_vectorizer.pkl")
print("Accuracy: ", accuracy)
print("Classification Report:\n", classification_report(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))