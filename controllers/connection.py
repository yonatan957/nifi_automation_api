from flask import Blueprint, jsonify, current_app, request

connection_bp = Blueprint('connections', __name__, url_prefix='/connections')

@connection_bp.route('', methods=['POST'])
def create_connection():
    nifi_service = current_app.config['nifi_service']
    service = not nifi_service
    return jsonify(service)