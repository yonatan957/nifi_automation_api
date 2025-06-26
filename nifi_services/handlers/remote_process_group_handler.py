from nifi_objects.general_objects import Port, InputPort, OutPutPort
from nifi_services.types import PortType

class RemoteProcessGroupHandler:

    def __init__(self, nifi_request, validate_response_status):
        self.nifi_request = nifi_request
        self.validate_response_status = validate_response_status