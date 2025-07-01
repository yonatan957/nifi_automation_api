from flask import Blueprint, jsonify, current_app, request
from controllers.controllers_utils import validated_payload
from nifi_objects.general_objects import ParameterContext

parameter_context_bp = Blueprint('parameter-contexts', __name__, url_prefix='/parameter-contexts')

@parameter_context_bp.route("", methods=["POST"])
def create_parameter_context():
    parameter_context = validated_payload(request, ParameterContext, 'failed to create parameter-context')
    nifi_service = current_app.config['nifi_service']
    new_parameter_context = nifi_service.create_parameter_context(parameter_context)
    return new_parameter_context