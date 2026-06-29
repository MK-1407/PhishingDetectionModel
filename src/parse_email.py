import re


def clean_text(text: str) -> str:
    if not text:
        return ""

    text = text.lower()
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def contains_url(text: str) -> int:
    return int(bool(re.search(r"https?://\S+|www\.\S+", text)))


def parse_email(email: str):
    email = email.strip()

    subject = ""
    body = email

    lines = email.splitlines()

    if lines and lines[0].lower().startswith("subject:"):
        subject = lines[0][8:].strip()
        body = "\n".join(lines[1:])

    text = clean_text(subject + " " + body)

    return {
        "subject": subject,
        "body": body,
        "text": text,
        "url": contains_url(text),   # <-- fixed (url, not urls)
    }