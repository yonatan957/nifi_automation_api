from nifi_services.types import GenericDict, Request_Type
from nifi_objects.general_objects import Funnel
class FunnelHandler:

    def __init__(self, nifi_request, validate_response_status):
        self.nifi_request = nifi_request
        self.validate_response_status = validate_response_status

    def create_funnel(self,funnel:Funnel, father_id: str) -> Funnel:
        print(funnel)
        response = self.nifi_request(
            Request_Type.POST,
            f"/process-groups/{father_id}/funnels",
            json=funnel.dict()
        )
        self.validate_response_status(response,{200, 201}, "failed to create funnel")
        return response.json()