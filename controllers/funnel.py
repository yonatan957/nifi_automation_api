from flask import Blueprint, jsonify, current_app, request
from controllers.controllers_utils import validated_payload
from nifi_objects.funnel import Funnel
funnel_bp = Blueprint('funnels', __name__, url_prefix='/funnels')

@funnel_bp.route("/", methods=["POST"])
def create_funnel():
    funnel = validated_payload(request, Funnel, '')
    nifi_service = current_app.config['nifi_service']
    new_funnel = nifi_service.create_funnel(funnel)
    return jsonify(new_funnel.dict())