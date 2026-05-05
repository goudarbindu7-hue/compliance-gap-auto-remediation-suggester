
from flask import Blueprint, request, jsonify
from services.groq_client import call_groq
from services.cache import get, set
from middleware.sanitizer import sanitize_input
from services.formatters import recommend_fallback, safe_json_loads

recommend_bp = Blueprint('recommend', __name__)

@recommend_bp.route('/recommend', methods=['POST'])
def recommend():
    try:
        gap = sanitize_input(request.json.get("gap",""))
    except Exception:
        return jsonify({"error":"Invalid input"}), 400

    prompt = open("prompts/recommend.txt").read().format(gap=gap)

    cached = get(prompt)
    if cached:
        data = safe_json_loads(cached)
        if data:
            return jsonify({"recommendations": data, "is_cached": True})

    result = call_groq(prompt)
    if not result:
        return jsonify(recommend_fallback())

    data = safe_json_loads(result)
    if not data:
        return jsonify(recommend_fallback())

    set(prompt, result)
    return jsonify({"recommendations": data})
