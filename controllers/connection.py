from flask import Blueprint, jsonify, current_app, request
from controllers.controllers_utils import validated_payload
from nifi_objects.general_objects import Connection

connection_bp = Blueprint('connections', __name__, url_prefix='/connections')

@connection_bp.route('<father_id>', methods=['POST'])
def create_connection(father_id:str):
    nifi_service = current_app.config['nifi_service']
    connection = validated_payload(request, Connection, 'failed to create connection')
    new_connection = nifi_service.create_connection(connection, father_id)
    return jsonify(new_connection)