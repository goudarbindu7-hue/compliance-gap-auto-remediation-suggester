
from flask import Flask
from dotenv import load_dotenv
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from routes.describe import describe_bp
from routes.recommend import recommend_bp
from routes.report import report_bp
from routes.health import health_bp

load_dotenv()

def create_app():
    app = Flask(__name__)

    limiter = Limiter(key_func=get_remote_address, default_limits=["30 per minute"])
    limiter.init_app(app)

    @app.after_request
    def set_headers(response):
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["X-XSS-Protection"] = "1; mode=block"
        response.headers["Content-Security-Policy"] = "default-src 'self'"
        return response

    app.register_blueprint(describe_bp)
    app.register_blueprint(recommend_bp)
    app.register_blueprint(report_bp)
    app.register_blueprint(health_bp)
    return app

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
