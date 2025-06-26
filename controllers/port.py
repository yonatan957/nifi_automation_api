from flask import Blueprint, jsonify, current_app, request

ports_bp = Blueprint('ports', __name__, url_prefix='/ports')

@ports_bp.route("/<pg_id>/input-ports", methods=["POST"])
def create_input_port():
    json_body = request.get_json()
    nifi_service = current_app.config['nifi_service']
    input_port = nifi_service.create_input_port()
    return jsonify(input_port.dict())