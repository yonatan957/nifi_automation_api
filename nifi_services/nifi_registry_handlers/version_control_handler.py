from utils.consts import BUCKET_ID, FLOW_IDENTIFIER
from nifi_services.types import Request_Type

class VersionControlHandler:

    def __init__(self, nifi_registry_request, validate_response_status):
        self.nifi_registry_request = nifi_registry_request
        self.validate_response_status = validate_response_status

    def get_version_control(self):
        response = self.nifi_registry_request(Request_Type.GET, f'/buckets/{BUCKET_ID}/flows/{FLOW_IDENTIFIER}')
        self.validate_response_status(response, {200,201}, 'error get flow')
        return response.json()