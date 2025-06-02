# backend/app/__init__.py

import logging
from flask import Flask, jsonify, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
from flask_cors import CORS
from flask_talisman import Talisman
from .routes import bp
from .config import Config

# Metrics counter
process_counter = Counter("process_operations_total", "Total process operations")

def create_app():
    app = Flask(__name__)

    # Load config
    app.config.from_object(Config)

    # Security Headers
    Talisman(app)

    # CORS
    CORS(app)

    # Rate Limiting
    limiter = Limiter(get_remote_address, app=app, default_limits=[app.config["RATE_LIMIT_DEFAULT"]])

    # Logging
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
    )

    @app.before_request
    def before_request_logging():
        logging.info(f"Request: {request.method} {request.path} — from {request.remote_addr}")

    # Global Error Handler
    @app.errorhandler(Exception)
    def handle_exception(e):
        logging.error(f"Unhandled Exception: {str(e)}")
        return jsonify({"error": str(e)}), 500

    # Health check
    @app.route("/health")
    def health():
        logging.info("Health check accessed")
        return {"status": "ok"}, 200

    # Metrics endpoint
    @app.route("/metrics")
    def metrics():
        process_counter.inc()
        return generate_latest(), 200, {"Content-Type": CONTENT_TYPE_LATEST}

    # Register Blueprint
    app.register_blueprint(bp)

    return app
