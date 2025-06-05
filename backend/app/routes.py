# app/routes.py

from flask import Blueprint, request, jsonify
from app.models import db, Process

bp = Blueprint('processes', __name__)

@bp.route("/processes", methods=["GET"])
def get_processes():
    page = int(request.args.get("page", 1))
    per_page = int(request.args.get("per_page", 5))

    processes = Process.query.order_by(Process.id.desc()).paginate(page=page, per_page=per_page, error_out=False)

    return jsonify({
        "page": page,
        "per_page": per_page,
        "total": processes.total,
        "processes": [p.to_dict() for p in processes.items]
    })

@bp.route("/processes", methods=["POST"])
def add_process():
    data = request.get_json()
    new_process = Process(
        name=data["name"],
        priority=data["priority"],
        timestamp=data["timestamp"]
    )
    db.session.add(new_process)
    db.session.commit()
    return jsonify(new_process.to_dict()), 201

@bp.route("/processes/<int:process_id>", methods=["DELETE"])
def delete_process(process_id):
    process = Process.query.get_or_404(process_id)
    db.session.delete(process)
    db.session.commit()
    return jsonify({"message": "Deleted"}), 200
