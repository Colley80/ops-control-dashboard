# app/__init__.py

import logging
from flask import Flask
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_talisman import Talisman
from app.config import Config
from app.middleware import before_request_logging, after_request_logging, register_error_handlers
from app.metrics import process_count
from app.models import db  # ADD THIS

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Security
    Talisman(app)
    CORS(app)

    # DB
    db.init_app(app)

    # Logging
    app.before_request(before_request_logging)
    app.after_request(after_request_logging)
    register_error_handlers(app)

    # Limiter
    limiter = Limiter(
        get_remote_address,
        app=app,
        default_limits=[Config.RATELIMIT_DEFAULT]
    )

    # Register Blueprints
    from app.routes import bp
    app.register_blueprint(bp)

    return app
