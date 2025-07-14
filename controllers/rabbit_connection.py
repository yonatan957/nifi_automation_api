from flask import Blueprint, jsonify, current_app, request
from controllers.controllers_utils import validated_payload
from nifi_objects.connection_details import ConnectionDetails

rabbit_bp = Blueprint('rabbit', __name__, url_prefix='/rabbit')

@funnel_bp.route("/connect", methods=["POST"])
def create_funnel():
    connection_details = validated_payload(request, Funnel, 'failed to get connection details')
    nifi_service = current_app.config['nifi_service']
    return