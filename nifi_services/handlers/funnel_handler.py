from nifi_services.types import GenericDict
from nifi_services.types import GenericDict, Request_Type
class FunnelHandler:

    def __init__(self, nifi_request, validate_response_status):
        self.nifi_request = nifi_request
        self.validate_response_status = validate_response_status

    def create_funnel(self, process_group_id: str) -> str:
        response = self.nifi_request(
            Request_Type.POST,
            f"/process-groups/{process_group_id}/funnels",
            json=self.create_funnel_payload()
        )
        self.validate_response_status(response,{200, 201}, "failed to create funnel")
        new_funnel = response.json()
        return new_funnel["id"]

    def create_funnel_payload(self, x_position:float = 400.0, y_position:float = 200.0) -> GenericDict:
        return {
            "revision": {"version": 0},
            "component": {
                "position": {"x": x_position, "y": y_position}
            }
        }
