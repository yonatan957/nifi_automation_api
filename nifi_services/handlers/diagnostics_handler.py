from typing import TypedDict
from nifi_services.types import Request_Type

class ConnectionHandler:
    def __init__(self, nifi_request, validate_response_status):
        self.nifi_request = nifi_request
        self.validate_response_status = validate_response_status
    class ConnectionResult(TypedDict):
        succeeded: bool
        message: str
    def is_nifi_connection_alive(self) -> ConnectionResult:
        response = self.nifi_request(Request_Type.GET, "/flow/about")
        self.validate_response_status(response, {200, 201}, "failed to connect nifi")
        return {"succeeded": True, "message": "Nifi connection is alive and ready"}