from nifi_objects.general_objects import ParameterContext
from nifi_services.types import GenericDict, Request_Type


class ParameterContextHandler:

    def __init__(self, nifi_request, validate_response_status):
        self.nifi_request = nifi_request
        self.validate_response_status = validate_response_status

    def create_parameter_context(self, parameter_context:ParameterContext, father_id: str):
        response = self.nifi_request(
            Request_Type.POST,
            f'/parameter-context',
            json=parameter_context.dict()
        )
        self.validate_response_status(response, {200, 201}, 'failed to create parameter context')
        return response.json()
