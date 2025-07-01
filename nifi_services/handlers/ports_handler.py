from nifi_services.types import GenericDict, Request_Type
from nifi_objects.port import Port, InputPort, OutPutPort
from nifi_services.types import PortType
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

    def get_all_ports(self, port_type: PortType, father_id:str):
        end_of_url = 'input-ports' if port_type == PortType.INPUT_PORT else 'output-ports'
        response = self.nifi_request(
            Request_Type.GET,
            f'/process-groups/{father_id}/{end_of_url}'
        )
        self.validate_response_status(response, {200, 201}, 'failed to get all ports')
        return response.json()