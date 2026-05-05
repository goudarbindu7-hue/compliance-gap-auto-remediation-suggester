
from flask import Blueprint, request, jsonify
from services.groq_client import call_groq
from services.cache import get, set
from middleware.sanitizer import sanitize_input
from services.formatters import describe_fallback
import time

describe_bp = Blueprint('describe', __name__)

@describe_bp.route('/describe', methods=['POST'])
def describe():
    try:
        gap = sanitize_input(request.json.get("gap",""))
    except Exception:
        return jsonify({"error":"Invalid input"}), 400

    prompt = open("prompts/describe.txt").read().format(gap=gap)

    cached = get(prompt)
    if cached:
        return jsonify({"description": cached, "generated_at": int(time.time()), "is_cached": True})

    result = call_groq(prompt)
    if not result:
        return jsonify(describe_fallback()), 200

    set(prompt, result)
    return jsonify({"description": result, "generated_at": int(time.time())})
