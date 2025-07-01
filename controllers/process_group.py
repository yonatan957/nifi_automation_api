from flask import Blueprint, jsonify, current_app, request
from nifi_objects.general_objects import ProcessGroup, ProcessGroupWithPorts, RemoteProcessGroup
from nifi_services.nifi_service import NifiService
from controllers.controllers_utils import validated_payload

process_group_bp = Blueprint('process_groups', __name__, url_prefix='/process-groups')

@process_group_bp.route('/<pg_id>', methods=["GET"])
def get_process_group(pg_id: str):
    nifi_service = current_app.config['nifi_service']
    process_group = nifi_service.get_process_group(pg_id)
    return jsonify(process_group)

@process_group_bp.route('/<pg_id>/get-all', methods=['GET'])
def get_all_process_group(pg_id: str):
    nifi_service:NifiService = current_app.config['nifi_service']
    process_groups = nifi_service.get_all_process_groups(pg_id)
    return jsonify(process_groups)

@process_group_bp.route('/root', methods=["GET"])
def get_root_id():
    nifi_service:NifiService = current_app.config['nifi_service']
    return jsonify({"id": nifi_service.get_root_id()})

@process_group_bp.route("/<father_id>", methods=["POST"])
def create_process_group(father_id: str):
    nifi_service:NifiService = current_app.config['nifi_service']
    process_group = validated_payload(request, ProcessGroup, 'invalid input on create-process-group')
    new_process_group = nifi_service.create_process_group(process_group, father_id)
    return jsonify(new_process_group)

@process_group_bp.route("/<father_id>/process-with-ports", methods=["POST"])
def create_process_group_with_ports(father_id: str):
    nifi_service:NifiService = current_app.config['nifi_service']
    process_group_with_ports = validated_payload(request, ProcessGroupWithPorts, 'invalid input on create-process-group')
    new_process_group_with_ports = nifi_service.create_pg_with_ports(process_group_with_ports, father_id)
    return jsonify(new_process_group_with_ports)

@process_group_bp.route('/<father_id>', methods=['PUT'])
def update_process_group(father_id: str):
    nifi_service:NifiService = current_app.config['nifi_service']
    process_group = validated_payload(request, ProcessGroup, 'invalid input on update-process-group')
    updated_process_group = nifi_service.update_process_group(process_group, father_id)
    return jsonify(updated_process_group)

@process_group_bp.route('/<father_id>/connect', methods=['POST'])
def connect_two_pgs(father_id:str):
    nifi_service:NifiService = current_app.config['nifi_service']
    r_p_g = validated_payload(request, RemoteProcessGroup, 'invalid input on connect_process_groups')
    new_r_p_g = nifi_service.create_remote_process_group(r_p_g, father_id)
    return jsonify(new_r_p_g)