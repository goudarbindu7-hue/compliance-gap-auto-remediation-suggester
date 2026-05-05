
from flask import Blueprint, jsonify
import time

health_bp = Blueprint('health', __name__)
start = time.time()

@health_bp.route('/health', methods=['GET'])
def health():
    return jsonify({
        "status":"UP",
        "uptime": round(time.time()-start,2)
    })
