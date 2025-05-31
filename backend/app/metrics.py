# backend/app/metrics.py

from flask import Blueprint, jsonify
import time

bp_metrics = Blueprint("metrics", __name__)

# Simulate metrics (in real app → use Prometheus client)
start_time = time.time()
request_count = 0

@bp_metrics.before_app_request
def before_request():
    global request_count
    request_count += 1

@bp_metrics.route("/metrics", methods=["GET"])
def metrics():
    uptime = time.time() - start_time
    return jsonify({
        "uptime_seconds": int(uptime),
        "request_count": request_count
    }), 200
