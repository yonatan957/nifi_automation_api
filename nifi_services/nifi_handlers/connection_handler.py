from nifi_services.types import GenericDict, Request_Type
from nifi_objects.connection import Connection

class ConnectionHandler:

    def __init__(self, nifi_request, validate_response_status):
        self.nifi_request = nifi_request
        self.validate_response_status = validate_response_status

    def create_connection(self, connection: Connection, father_id:str):
        response = self.nifi_request(
            Request_Type.POST,
            f"/process-groups/{father_id}/connections",
            json=connection.model_dump(mode="json")
        )
        self.validate_response_status(response, {200, 201}, "failed to create connection")
        return response.json()