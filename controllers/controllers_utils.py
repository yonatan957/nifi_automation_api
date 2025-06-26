from flask import request
from error.errors import BadRequestError
def validated_payload(request_to_validate: request, object_to_convert, message="Bad request"):
    try:
        return_object = object_to_convert(**request_to_validate.json())
        return return_object
    except Exception:
        raise BadRequestError(message)