from nifi_objects.process_group import ProcessGroup
class ProcessGroupHandler:

    def __init__(self, nifi_request, validate_response_status):
        self.nifi_request = nifi_request
        self.validate_response_status = validate_response_status

    def get_root_id(self) -> str:
        response = self.nifi_request(Request_Type.GET, "/flow/process-groups/root")
        self.validate_response_status(response, {200, 201}, "failed to get root id")
        root_pg = response.json()
        return root_pg["processGroupFlow"]["id"]

    def create_process_group(self, name: str, father_id: str) -> ProcessGroup:
        response = self.nifi_request(
            Request_Type.POST,
            f"/process-groups/{father_id}/process-groups",
            json=self.create_pg_payload(name)
        )
        self.validate_response_status(response, {200, 201}, "failed to create process group")
        return ProcessGroup(**response.json())

    def get_process_group(self, pg_id: str) -> ProcessGroup:
        response = self.nifi_request(Request_Type.GET, f"/process-groups/{pg_id}")
        self.validate_response_status(response, {200}, "failed to get process group")
        return ProcessGroup(**response.json())

    def create_pg_payload(self, name: str, x_position: float = 400.0, y_position: float = 200.0) -> GenericDict:
        return {
            "revision": {"version": 0},
            "component": {
                "name": name,
                "position": {"x": x_position, "y": y_position}
            }
        }