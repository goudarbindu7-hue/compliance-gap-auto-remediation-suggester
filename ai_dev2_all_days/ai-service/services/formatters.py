
import json

def safe_json_loads(text):
    try:
        return json.loads(text)
    except Exception:
        return None

def describe_fallback():
    return {
        "description": "Unable to generate description at this time.",
        "generated_at": None,
        "is_fallback": True
    }

def recommend_fallback():
    return {
        "recommendations": [
            {"action_type": "MANUAL_REVIEW", "description": "Review configuration manually.", "priority": "MEDIUM"}
        ],
        "is_fallback": True
    }

def report_fallback():
    return {
        "title": "Compliance Report (Fallback)",
        "summary": "AI unavailable. Please retry later.",
        "overview": "",
        "key_items": [],
        "recommendations": [],
        "is_fallback": True
    }
