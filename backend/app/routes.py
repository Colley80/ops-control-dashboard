# app/routes.py

from flask import Blueprint, jsonify, request
from app.metrics import process_count

bp = Blueprint('processes', __name__)

# In-memory "database"
process_db = []
process_id_counter = 1

@bp.route('/processes', methods=['GET'])
def get_processes():
    global process_db
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 5))
    sort_by = request.args.get('sort_by', 'id')

    sorted_processes = sorted(process_db, key=lambda x: x.get(sort_by, ''))
    start = (page - 1) * per_page
    end = start + per_page
    paginated = sorted_processes[start:end]

    return jsonify({
        'page': page,
        'per_page': per_page,
        'total': len(process_db),
        'processes': paginated
    }), 200

@bp.route('/processes', methods=['POST'])
def add_process():
    global process_db, process_id_counter
    data = request.json
    new_process = {
        'id': process_id_counter,
        'name': data.get('name', ''),
        'priority': data.get('priority', 'Medium'),
        'timestamp': data.get('timestamp', '')
    }
    process_db.append(new_process)
    process_id_counter += 1
    process_count.inc()

    return jsonify(new_process), 201

@bp.route('/processes/<int:process_id>', methods=['DELETE'])
def delete_process(process_id):
    global process_db
    process_db = [p for p in process_db if p['id'] != process_id]
    process_count.dec()

    return jsonify({'message': 'Process deleted'}), 200
