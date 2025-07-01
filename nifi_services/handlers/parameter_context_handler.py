from nifi_objects import ParameterContext
from nifi_services.types import GenericDict, Request_Type


class ParameterContextHandler:

    def __init__(self, nifi_request, validate_response_status):
        self.nifi_request = nifi_request
        self.validate_response_status = validate_response_status

    def create_parameter_context(self, parameter_context:ParameterContext):
        response = self.nifi_request(
            Request_Type.POST,
            f'/parameter-contexts',
            json=parameter_context.dict()
        )
        self.validate_response_status(response, {200, 201}, 'failed to create parameter context')
        return response.json()

    def update_parameter_context(self, context_id:str, parameter_context:ParameterContext):
        response = self.nifi_request(
            Request_Type.POST,
            f'/parameter-contexts/{context_id}/update-requests',
            json=parameter_context.dict()
        )
        self.validate_response_status(response, {200,201}, 'failed to update parameter context')
        return response.json()