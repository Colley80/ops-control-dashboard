# app/routes.py

from flask import Blueprint, jsonify, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

bp = Blueprint("processes", __name__)

# In-memory "database" for now
processes = []

# Initialize limiter
limiter = Limiter(key_func=get_remote_address)

# GET with pagination and sorting
@bp.route("/processes", methods=["GET"])
@limiter.limit("10 per minute")
def get_processes():
    sort_by = request.args.get("sort_by", "id")
    page = int(request.args.get("page", 1))
    per_page = int(request.args.get("per_page", 5))

    sorted_processes = sorted(
        processes,
        key=lambda x: x.get(sort_by, ""),
    )

    start = (page - 1) * per_page
    end = start + per_page
    paged = sorted_processes[start:end]

    return jsonify({
        "page": page,
        "per_page": per_page,
        "total": len(processes),
        "processes": paged
    }), 200

# POST
@bp.route("/processes", methods=["POST"])
@limiter.limit("5 per minute")
def add_process():
    data = request.get_json()

    if not data or "name" not in data:
        return {"error": "Missing process name"}, 400

    new_process = {
        "id": len(processes) + 1,
        "name": data["name"],
        "priority": data.get("priority", "Normal"),
        "timestamp": data.get("timestamp", "N/A")
    }

    processes.append(new_process)

    return jsonify(new_process), 201

# DELETE
@bp.route("/processes/<int:process_id>", methods=["DELETE"])
@limiter.limit("5 per minute")
def delete_process(process_id):
    global processes
    processes = [p for p in processes if p["id"] != process_id]
    return jsonify({"message": f"Process {process_id} deleted"}), 200

