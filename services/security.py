import re

def sanitize(text):
    return re.sub(r"<.*?>", "", text)

def detect_injection(text):
    return "ignore" in text.lower()
