from flask import Blueprint, jsonify, current_app, request
from controllers.controllers_utils import validated_payload
from nifi_objects.general_objects import Funnel

funnel_bp = Blueprint('funnels', __name__, url_prefix='/funnels')

@funnel_bp.route("/<father_id>", methods=["POST"])
def create_funnel(father_id:str):
    funnel = validated_payload(request, Funnel, 'failed to create funnel')
    nifi_service = current_app.config['nifi_service']
    new_funnel = nifi_service.create_funnel(funnel, father_id)
    return jsonify(new_funnel)