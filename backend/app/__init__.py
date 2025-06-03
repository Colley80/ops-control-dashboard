# app/__init__.py

import os
import logging
from flask import Flask, request
from flask_cors import CORS
from flask_talisman import Talisman
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from dotenv import load_dotenv
from prometheus_client import make_wsgi_app
from werkzeug.middleware.dispatcher import DispatcherMiddleware

# Load .env
load_dotenv()

# Import middleware hooks
from app.middleware import before_request_logging, after_request_logging, register_error_handlers

# Import routes AFTER limiter is defined (no circular import)
from app.routes import bp

# Import metrics
from app.metrics import process_count

# Configure logging
if not os.path.exists('logs'):
    os.makedirs('logs')

logging.basicConfig(
    filename='logs/app.log',
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Initialize Limiter — needs to be global so routes can use it
limiter = Limiter(
    key_func=get_remote_address,
    default_limits=["100 per minute"],
    storage_uri="memory://"
)

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev')

    # Security headers
    Talisman(app)

    # CORS (allow frontend)
    CORS(app, resources={r"/*": {"origins": os.getenv('FRONTEND_URL', 'http://localhost:5173')}})

    # Register rate limiter
    limiter.init_app(app)

    # Register middleware hooks
    app.before_request(before_request_logging)
    app.after_request(after_request_logging)
    register_error_handlers(app)

    # Register routes
    app.register_blueprint(bp)

    # Add Prometheus metrics endpoint
    app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
        '/metrics': make_wsgi_app()
    })

    return app
