from flask import request
from error.errors import BadRequestError
from utils.logger import logger
def validated_payload(request_to_validate: request, object_to_convert, message="Bad request"):
    try:
        return_object = object_to_convert(**request_to_validate.get_json())
        return return_object
    except Exception as e:
        logger.error(str(e))
        raise BadRequestError(message)