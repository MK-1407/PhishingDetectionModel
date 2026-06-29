# 🛡️ Phishing Detection Model

A Python-based phishing email detector that classifies emails as **Safe** or **Phishing** using **TF-IDF vectorization**, **URL feature extraction**, and a **Logistic Regression** model built with **Scikit-learn**.

## Features

* 📧 Detects phishing emails from raw email text.
* 🧹 Automatic email preprocessing and parsing.
* 🔗 Extracts URL presence as an additional feature.
* 🤖 Uses TF-IDF vectorization for text representation.
* 🧠 Logistic Regression classifier trained with Scikit-learn.
* 🖥️ Interactive command-line interface powered by Rich.

## Tech Stack

* Python
* Scikit-learn
* Pandas
* NumPy
* SciPy
* Rich
* Joblib

## Project Structure

```text
PhishingDetectionModel/
│
├── model/
│   ├── logistic_model.pkl
│   └── tfidf_vectorizer.pkl
│
├── src/
│   ├── detect.py
│   ├── parse_email.py
│   └── ...
│
├── main.py
├── requirements.txt
└── README.md
```

## How It Works

1. Paste a raw email into the application.
2. The email is automatically parsed to extract:

   * Subject
   * Body
   * URL presence
3. The text is cleaned and transformed using TF-IDF.
4. The Logistic Regression model predicts whether the email is **Safe** or **Phishing**.
5. The prediction confidence is displayed to the user.

## Installation

```bash
git clone https://github.com/MK-1407/PhishingDetectionModel.git

cd PhishingDetectionModel

pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

Paste the complete email and type `END` on a new line to finish input.

## Dataset

The training dataset is **not included** in this repository due to GitHub's file size limitations.

You may recreate the dataset using publicly available phishing email datasets and retrain the model if desired.

## Future Improvements

* HTML email analysis
* Sender reputation analysis
* Attachment inspection
* Additional email header features
* Deep learning models (LSTM/BERT)
* Graphical User Interface

## License

This project is licensed under the MIT License.
