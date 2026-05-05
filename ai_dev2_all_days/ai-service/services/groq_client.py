
import os, requests, time

URL = "https://api.groq.com/openai/v1/chat/completions"

def call_groq(prompt: str):
    api_key = os.getenv("GROQ_API_KEY")
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": os.getenv("GROQ_MODEL", "llama3-70b-8192"),
        "messages": [{"role": "user", "content": prompt}],
        "temperature": float(os.getenv("GROQ_TEMPERATURE", "0.3")),
        "max_tokens": int(os.getenv("GROQ_MAX_TOKENS", "800"))
    }
    for i in range(3):
        try:
            res = requests.post(URL, json=payload, headers=headers, timeout=10)
            res.raise_for_status()
            data = res.json()
            return data["choices"][0]["message"]["content"]
        except Exception:
            time.sleep(2 ** i)
    return None
