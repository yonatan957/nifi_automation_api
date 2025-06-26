from nifi_services.types import GenericDict, Request_Type
from nifi_objects.general_objects import Port, InputPort, OutPutPort
class PortsHandler:
    def __init__(self, nifi_request, validate_response_status):
        self.nifi_request = nifi_request
        self.validate_response_status = validate_response_status

    def create_port(self, port: Port, father_id: str):
        end_of_url = 'input-ports' if isinstance(port, InputPort) else 'output-ports'
        response = self.nifi_request(
            Request_Type.POST,
            f"/process-groups/{father_id}/{end_of_url}",
            json=port.dict())

        self.validate_response_status(response, {200, 201}, 'failed to create port')
        return response.json()