from nifi_objects.general_objects import RemoteProcessGroup
from nifi_services.types import Request_Type

class RemoteProcessGroupHandler:

    def __init__(self, nifi_request, validate_response_status):
        self.nifi_request = nifi_request
        self.validate_response_status = validate_response_status

    def create_remote_process_group(self, remote_pg:RemoteProcessGroup, father_id:str):
        response = self.nifi_request(
            Request_Type.POST,
            f'/process-groups/{father_id}/remote-process-groups',
            json=remote_pg.dict()
        )
        self.validate_response_status(response, {200,  201}, 'failed to create port')
        return response.json()