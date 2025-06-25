from flask import Blueprint, jsonify, current_app, request

funnel_bp = Blueprint('funnels', __name__, url_prefix='/funnels')

@funnel_bp.route("/", methods=["POST"])
def create_funnel():
    json_body = request.get_json()
    nifi_service = current_app.config['nifi_service']
    new_funnel = nifi_service.create_funnel(json_body["father_id"])
    return jsonify(new_funnel.dict())