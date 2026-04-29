from flask import Blueprint, request, jsonify
from services.groq_client import GroqClient
from services.security import sanitize, detect_injection

report_bp = Blueprint("report", __name__)
client = GroqClient()

@report_bp.route("/generate-report", methods=["POST"])
def generate_report():
    data = request.json
    text = data.get("text", "")

    clean = sanitize(text)

    if detect_injection(clean):
        return jsonify({"error": "Injection detected"}), 400

    result = client.generate(clean)

    return jsonify({"result": result})
