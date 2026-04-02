class APIError(Exception):
    status_code = 500

    def __init__(self, message=None, status_code=None):
        super().__init__(message)
        if message:
            self.message = message
        else:
            self.message = "An error occurred"

        if status_code:
            self.status_code = status_code

    def to_dict(self):
        return {
            "error": self.__class__.__name__,
            "message": self.message
        }


class NotFoundError(APIError):
    status_code = 404

    def __init__(self, message="Resource not found"):
        super().__init__(message, self.status_code)


class BadRequestError(APIError):
    status_code = 400

    def __init__(self, message="Bad request"):
        super().__init__(message, self.status_code)


class UnauthorizedError(APIError):
    status_code = 401

    def __init__(self, message="Unauthorized"):
        super().__init__(message, self.status_code)


class ForbiddenError(APIError):
    status_code = 403

    def __init__(self, message="Forbidden"):
        super().__init__(message, self.status_code)


class InternalServerError(APIError):
    status_code = 500

    def __init__(self, message="Internal server error"):
        super().__init__(message, self.status_code)