import pandas as pd


def prepare_subject_body_dataset(path):
    df = pd.read_csv(path)

    df["subject"] = df["subject"].fillna("")
    df["body"] = df["body"].fillna("")

    df["text"] = df["subject"] + " " + df["body"]

    if "urls" not in df.columns:
        df["urls"] = (
            df["text"]
            .str.contains(r"https?://|www\.", regex=True)
            .astype(int)
        )

    return df[["text", "urls", "label"]]


def prepare_text_dataset(path):
    df = pd.read_csv(path)

    df["text"] = df["text_combined"].fillna("")

    df["urls"] = (
        df["text"]
        .str.contains(r"https?://|www\.", regex=True)
        .astype(int)
    )

    return df[["text", "urls", "label"]]


datasets = [
    prepare_subject_body_dataset("datasets/CEAS_08.csv"),
    prepare_subject_body_dataset("datasets/Enron.csv"),
    prepare_subject_body_dataset("datasets/Ling.csv"),
    prepare_subject_body_dataset("datasets/Nazario.csv"),
    prepare_subject_body_dataset("datasets/Nigerian_Fraud.csv"),
    prepare_subject_body_dataset("datasets/SpamAssasin.csv"),
    prepare_text_dataset("datasets/phishing_email.csv"),
]

merged_df = pd.concat(datasets, ignore_index=True)

merged_df = merged_df.sample(
    frac=1,
    random_state=42
).reset_index(drop=True)

merged_df.to_csv(
    "datasets/merged_dataset.csv",
    index=False
)

print("=" * 50)
print("Merged Successfully!")
print("=" * 50)
print(f"Total Emails : {len(merged_df)}")
print()
print(merged_df["label"].value_counts())