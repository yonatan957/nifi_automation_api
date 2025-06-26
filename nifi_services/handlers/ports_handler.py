from nifi_services.types import GenericDict, Request_Type

class PortsHandler:
    def __init__(self, nifi_request, validate_response_status):
        self.nifi_request = nifi_request
        self.validate_response_status = validate_response_status

    def create_input_port(self, father_id:str, input_port:GenericDict):
        response = self.nifi_request(
            Request_Type.POST,
            f"/process-groups/{father_id}/input-ports",
            json=input_port)

        self.validate_response_status(response, {200}, 'failed to create input port')
        return input_port