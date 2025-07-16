from nifi_objects.process_group import ProcessGroup
from nifi_services.types import GenericDict, Request_Type

class ProcessGroupHandler:

    def __init__(self, nifi_request, validate_response_status):
        self.nifi_request = nifi_request
        self.validate_response_status = validate_response_status

    def get_root_id(self) -> str:
        response = self.nifi_request(Request_Type.GET, "/flow/process-groups/root")
        self.validate_response_status(response, {200, 201}, "failed to get root id")
        root_pg = response.json()
        return root_pg["processGroupFlow"]["id"]

    def create_process_group(self, process_group:ProcessGroup, father_id: str) -> ProcessGroup:
        response = self.nifi_request(
            Request_Type.POST,
            f"/process-groups/{father_id}/process-groups",
            json=process_group.dict()
        )
        self.validate_response_status(response, {200, 201}, "failed to create process group")
        return response.json()

    def get_process_group(self, pg_id: str):
        response = self.nifi_request(Request_Type.GET, f"/process-groups/{pg_id}")
        self.validate_response_status(response, {200, 201}, "failed to get process group")
        return response.json()

    def update_process_group(self, process_group:ProcessGroup):
        response = self.nifi_request(Request_Type.PUT, f'/process-groups/{process_group.id}', json=process_group.dict())
        self.validate_response_status(response, {200, 201}, 'failed to update process group')
        return response.json()

    def get_all_process_groups(self, father_id):
        response = self.nifi_request(Request_Type.GET, f'/process-groups/{father_id}/process-groups')
        self.validate_response_status(response, {200,201}, 'failed to get all process groups')
        return response.json()