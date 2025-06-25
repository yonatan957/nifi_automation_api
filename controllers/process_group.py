from flask import Blueprint, jsonify, current_app, request

process_group_bp = Blueprint('process_groups', __name__, url_prefix='/process-groups')

@process_group_bp.route('/<pg_id>', methods=["GET"])
def get_process_group(pg_id: str):
    nifi_service = current_app.config['nifi_service']
    process_group = nifi_service.get_process_group(pg_id)
    return jsonify(process_group.dict())

@process_group_bp.route('/root', methods=["GET"])
def get_root_id():
    nifi_service = current_app.config['nifi_service']
    return jsonify({"id": nifi_service.get_root_id()})

@process_group_bp.route("/<father_id>", methods=["POST"])
def create_process_group(father_id: str):
    process_group_json = request.get_json()
    nifi_service = current_app.config['nifi_service']
    new_process_group = nifi_service.create_process_group(process_group_json, father_id)
    return jsonify(new_process_group.dict())

@process_group_bp.route('/<father_id>', methods=['PUT'])
def update_process_group(father_id: str):
    process_group_json = request.get_json()
    nifi_service = current_app.config['nifi_service']
    process_group = nifi_service.update_process_group(process_group_json, father_id)
    return jsonify(process_group.dict())