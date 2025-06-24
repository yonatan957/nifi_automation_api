import requests
from typing import Set, Optional
from utils.logger import logger
from requests import Response
from nifi_services.types import Request_Type, GenericDict
from nifi_services.handlers.process_group_handler import ProcessGroupHandler
from nifi_services.handlers.funnel_handler import FunnelHandler
from nifi_services.handlers.diagnostics_handler import DiagnosticsHandler

class NifiService:
    def __init__(self, base_url: str, username: str, password: str, verify_ssl: bool = True):
        self.base_url = base_url.rstrip('/')
        self.username = username
        self.password = password
        self.verify_ssl = verify_ssl
        self.token = self._get_token()

        self.process_group_handler = ProcessGroupHandler(self.nifi_request, self.validate_response_status)
        self.diagnostics_handler = DiagnosticsHandler(self.nifi_request, self.validate_response_status)
        self.funnel_handler = FunnelHandler(self.nifi_request, self.validate_response_status)

    def validate_response_status(self, response: Response, valid_statuses: Set[int], error_message:str) -> None:
        if response.status_code not in valid_statuses:
            full_message = (
                f"{error_message}\n"
                f"Status Code: {response.status_code}\n"
                f"Response Text: {response.text}"
            ).strip()
            logger.error(full_message)
            raise Exception(full_message)

    def _get_token(self) -> str:
        response = requests.post(f'{self.base_url}/access/token', data={"username": self.username, "password": self.password}, verify=self.verify_ssl)
        self.validate_response_status(response, {200,201}, "failed to get token")
        return response.text.strip()

    # I know that recursion is usually bad practice, but here I think it's readable and better.
    def nifi_request(self, method: Request_Type, url: str = "", *, json: Optional[GenericDict] = None,
                     data: Optional[GenericDict] = None, params: Optional[GenericDict] = None, retry_count=1
                     ) -> requests.Response:
        """
        a generic function for create request to nifi_services, using the constants TOKEN, VERIFY (if we want
        secure requests or not, locally not), and trying again if you were unauthorized with another
        token, recursively, as many times as you want, with field "retry_count"
        :param method: the method for the request, of type :class:`Request_Type`
        :param url: the end of the url to use initial empty
        :param json: if you want to send json in body - An object of type Parameter_Type with unlimited (arbitrary) keys.
        :param data: if you want to send file in body - An object of type Parameter_Type with unlimited (arbitrary) keys.
        :param params: if you want to send with query params - An object of type Parameter_Type with unlimited (arbitrary) keys.
        :param retry_count: how many times you want the function will try again with another token in
        case of authentication failed, initially 1
        :return: the response from the server
        """
        res = requests.request(method=method.value, url=f"{self.base_url}{url}", verify=self.verify_ssl,
                               headers={"Authorization": f"Bearer {self.token}"}, json=json, data=data, params=params)
        if res.status_code == 401 and retry_count > 0:
            self.token = self._get_token()
            return self.nifi_request(method, url, json=json, data=data, params=params, retry_count=retry_count - 1)
        return res

    def is_nifi_connection_alive(self):
        return self.diagnostics_handler.is_nifi_connection_alive()

    def get_root_id(self):
        return self.process_group_handler.get_root_id()

    def create_process_group(self, name:str, father_id:str):
        return self.process_group_handler.create_process_group(name, father_id)

    def get_process_group(self, pg_id:str):
        return self.process_group_handler.get_process_group(pg_id)

    def create_funnel(self, process_group_id:str):
        return self.funnel_handler.create_funnel(process_group_id)