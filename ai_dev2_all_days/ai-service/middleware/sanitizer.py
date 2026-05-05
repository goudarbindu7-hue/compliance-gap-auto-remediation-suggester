
import re

INJECTION_PATTERNS = [
    r"ignore instructions",
    r"act as system",
    r"override",
    r"system prompt",
]

def sanitize_input(text: str) -> str:
    if not text:
        return ""
    text = re.sub(r"<.*?>", "", text)
    lowered = text.lower()
    for p in INJECTION_PATTERNS:
        if re.search(p, lowered):
            raise ValueError("Prompt injection detected")
    return text.strip()
