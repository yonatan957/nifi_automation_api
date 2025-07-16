from flask import Blueprint, jsonify, current_app, request
from controllers.controllers_utils import validated_payload
from nifi_objects.parameter_context import ParameterContext
from nifi_services.nifi_service import NifiService

parameter_context_bp = Blueprint('parameter-contexts', __name__, url_prefix='/parameter-contexts')

@parameter_context_bp.route("", methods=["POST"])
def create_parameter_context():
    parameter_context = validated_payload(request, ParameterContext, 'failed to create parameter-context')
    nifi_service:NifiService = current_app.config['nifi_service']
    new_parameter_context = nifi_service.create_parameter_context(parameter_context)
    return new_parameter_context

@parameter_context_bp.route('<context_id>/update-requests', methods=['POST'])
def update_parameter_context(context_id:str):
    parameter_context = validated_payload(request, ParameterContext, 'payload error: check your request')
    nifi_service:NifiService = current_app.config['nifi_service']
    updated_parameter_context = nifi_service.update_parameter_context(context_id, parameter_context)
    return updated_parameter_context