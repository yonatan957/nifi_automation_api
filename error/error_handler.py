from flask import jsonify, Flask
from errors import APIError
from utils.logger import logger
def register_error_handlers(app: Flask) -> None:
    @app.errorhandler(APIError)
    def handle_api_error(error:APIError):
        response = jsonify(error.to_dict())
        response.status_code = error.status_code
        return response

    @app.errorhandler(500)
    def handle_internal_error(error):
        logger.error(str(error))
        response = jsonify({
            "error": "InternalServerError",
            "message": "Internal server error occurred"
        })
        response.status_code = 500
        return response