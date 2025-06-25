from flask import Blueprint, jsonify, current_app

process_group_bp = Blueprint('process_groups', __name__, url_prefix='/process-groups')


@process_group_bp.route('/root_id', methods=["GET"])
def get_root_id():
    try:
        nifi_service = current_app.config['nifi_service']
        return jsonify({"id": nifi_service.get_root_id()})
    except Exception as e:
        return