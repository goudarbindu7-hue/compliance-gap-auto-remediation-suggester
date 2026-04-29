from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
limiter = Limiter(get_remote_address, app=app, default_limits=["30 per minute"])

from routes.generate_report import report_bp
from routes.health import health_bp

app.register_blueprint(report_bp)
app.register_blueprint(health_bp)

if __name__ == "__main__":
    app.run(port=5000)
