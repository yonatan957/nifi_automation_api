from flask import Blueprint, jsonify, current_app, request
from nifi_services.version_control_service import VersionControlService
from controllers.controllers_utils import validated_payload
from nifi_objects.connection_details import ConnectionDetails

rabbit_bp = Blueprint('rabbit', __name__, url_prefix='/rabbit')

@rabbit_bp.route("/connect", methods=["POST"])
def create_funnel():
    version_control_service:VersionControlService = current_app.config["version_control_service"]
    connection_details = validated_payload(request, ConnectionDetails, 'failed to get connection details')
    return version_control_service.create_pg_from_version_control(connection_details)