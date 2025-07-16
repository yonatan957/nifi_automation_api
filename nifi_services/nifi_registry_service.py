from nifi_services.types import Request_Type
import requests
from nifi_services.nifi_registry_handlers.version_control_handler import VersionControlHandler
from requests import Response
from typing import Set, Optional
from nifi_services.types import Request_Type, GenericDict, PortType

class NifiRegistryService:

    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip('/')
        self.version_control_handler = VersionControlHandler(self.nifi_registry_request, self.validate_response_status)


    def validate_response_status(self, response: Response, valid_statuses: Set[int], error_message: str, status_error = None) -> None:
        if response.status_code not in valid_statuses:
            full_message = (
                f"{error_message}\n"
                f"Status Code: {response.status_code}\n"
                f"Response Text: {response.text}"
            ).strip()
            logger.error(full_message)
            status_error = status_error if status_error else response.status_code
            if status_error == 404:
                raise NotFoundError(full_message)
            elif status_error == 400:
                raise BadRequestError(full_message)
            else:
                raise APIError(full_message, status_code=response.status_code)

    def nifi_registry_request(self, method: Request_Type, url: str = "", *, json: Optional[GenericDict] = None,
                     data: Optional[GenericDict] = None, params: Optional[GenericDict] = None, retry_count=1
                     ) -> requests.Response:
        response = requests.request(method=method.value, url=f"{self.base_url}{url}",
                               json=json, data=data, params=params)
        return response

    def get_version_control(self):
        return self.version_control_handler.get_version_control()