from flask import Blueprint, jsonify, current_app, request
from controllers.controllers_utils import validated_payload
from nifi_objects.general_objects import Port, InputPort, OutPutPort
port_bp = Blueprint('ports', __name__, url_prefix='/ports')

@port_bp.route("/<father_id>/output-ports", methods=["POST"])
@port_bp.route("/<father_id>/input-ports", methods=["POST"])
def create_port(father_id:str):
    port_type = InputPort if '/input-ports' in request.path else OutPutPort
    port = validated_payload(request, port_type, 'failed to create port')
    nifi_service = current_app.config['nifi_service']
    new_port = nifi_service.create_port(port, father_id)
    return jsonify(new_port)