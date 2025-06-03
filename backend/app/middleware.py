# app/middleware.py

import logging
from flask import request, jsonify

def before_request_logging():
    logging.info(f"Request: {request.method} {request.path} — from {request.remote_addr}")

def after_request_logging(response):
    logging.info(f"Response: {response.status_code} {request.method} {request.path}")
    return response

def register_error_handlers(app):
    @app.errorhandler(404)
    def not_found_error(error):
        logging.error(f"Unhandled Exception: 404 Not Found: {error}")
        return jsonify({'error': 'Not Found'}), 404

    @app.errorhandler(429)
    def rate_limit_error(error):
        logging.error(f"Unhandled Exception: 429 Too Many Requests: {error}")
        return jsonify({'error': 'Too Many Requests'}), 429

    @app.errorhandler(Exception)
    def general_error(error):
        logging.error(f"Unhandled Exception: {error}")
        return jsonify({'error': 'Internal Server Error'}), 500
