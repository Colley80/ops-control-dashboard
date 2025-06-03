# app/routes.py

from flask import Blueprint, jsonify, request
from app.metrics import process_count
import logging

bp = Blueprint('processes', __name__)

# In-memory process store (for demo)
process_store = []
process_id_counter = 1

@bp.route('/processes', methods=['GET'])
def get_processes():
    try:
        logging.info("Fetching process list")

        # Optional pagination params
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 5))

        start = (page - 1) * per_page
        end = start + per_page

        paginated = process_store[start:end]

        response = {
            'page': page,
            'per_page': per_page,
            'total': len(process_store),
            'processes': paginated
        }

        return jsonify(response), 200

    except Exception as e:
        logging.error(f"Error fetching processes: {str(e)}")
        return jsonify({'error': 'Internal Server Error'}), 500

@bp.route('/processes', methods=['POST'])
def add_process():
    try:
        data = request.json
        global process_id_counter

        new_process = {
            'id': process_id_counter,
            'name': data.get('name'),
            'priority': data.get('priority'),
            'timestamp': data.get('timestamp')
        }

        process_store.append(new_process)
        process_id_counter += 1
        process_count.inc()

        logging.info(f"Process added: {new_process}")

        return jsonify(new_process), 201

    except Exception as e:
        logging.error(f"Error adding process: {str(e)}")
        return jsonify({'error': 'Internal Server Error'}), 500

@bp.route('/processes/<int:process_id>', methods=['DELETE'])
def delete_process(process_id):
    try:
        global process_store
        process_store = [p for p in process_store if p['id'] != process_id]
        logging.info(f"Process deleted: {process_id}")
        return jsonify({'message': 'Process deleted'}), 200

    except Exception as e:
        logging.error(f"Error deleting process: {str(e)}")
        return jsonify({'error': 'Internal Server Error'}), 500
