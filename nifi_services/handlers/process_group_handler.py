from nifi_objects.process_group import ProcessGroup
from nifi_services.types import GenericDict, Request_Type

type = Callable[[int, Optional[int]],str]
class ProcessGroupHandler:

    def __init__(self, nifi_request:type, validate_response_status):
        self.nifi_request = nifi_request
        self.validate_response_status = validate_response_status

    def get_root_id(self) -> str:
        response = self.nifi_request(Request_Type.GET, "/flow/process-groups/root")
        self.validate_response_status(response, {200, 201}, "failed to get root id")
        root_pg = response.json()
        return root_pg["processGroupFlow"]["id"]

    def create_process_group(self, process_group:GenericDict, father_id: str) -> ProcessGroup:
        response = self.nifi_request(
            Request_Type.POST,
            f"/process-groups/{father_id}/process-groups",
            json=process_group
        )
        self.validate_response_status(response, {200, 201}, "failed to create process group")
        return ProcessGroup(**response.json())

    def get_process_group(self, pg_id: str) -> ProcessGroup:
        response = self.nifi_request(Request_Type.GET, f"/process-groups/{pg_id}")
        self.validate_response_status(response, {200}, "failed to get process group")
        return ProcessGroup(**response.json())

    def update_process_group(self, process_group, father_id):
        response = self.nifi_request(Request_Type.PUT, f'/process-groups/{father_id}', json=process_group)
        self.validate_response_status(response, {200}, 'failed to update process group')
        return ProcessGroup(**response.json())