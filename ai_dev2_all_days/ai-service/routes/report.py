
from flask import Blueprint, request, jsonify
from services.groq_client import call_groq
from services.cache import get, set
from middleware.sanitizer import sanitize_input
from services.formatters import report_fallback, safe_json_loads

report_bp = Blueprint('report', __name__)

@report_bp.route('/generate-report', methods=['POST'])
def report():
    try:
        gap = sanitize_input(request.json.get("gap",""))
    except Exception:
        return jsonify({"error":"Invalid input"}), 400

    prompt = open("prompts/report.txt").read().format(gap=gap)

    cached = get(prompt)
    if cached:
        data = safe_json_loads(cached)
        if data:
            data["is_cached"] = True
            return jsonify(data)

    result = call_groq(prompt)
    if not result:
        return jsonify(report_fallback())

    data = safe_json_loads(result)
    if not data:
        return jsonify(report_fallback())

    set(prompt, result)
    return jsonify(data)
