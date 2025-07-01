import requests
from typing import Set, Optional
from utils.logger import logger
from requests import Response
from nifi_services.types import Request_Type, GenericDict, PortType
from nifi_objects.general_objects import ParameterContext
from nifi_services.handlers.process_group_handler import ProcessGroupHandler
from nifi_services.handlers.funnel_handler import FunnelHandler
from nifi_services.handlers.diagnostics_handler import DiagnosticsHandler
from nifi_services.handlers.ports_handler import PortsHandler
from nifi_services.handlers.remote_process_group_handler import RemoteProcessGroupHandler
from nifi_services.handlers.connection_handler import ConnectionHandler
from nifi_services.handlers.parameter_context_handler import ParameterContextHandler
from error.errors import UnauthorizedError, BadRequestError, APIError, NotFoundError
from nifi_objects.port import Port, InputPort, OutPutPort
from nifi_objects.funnel import Funnel
from nifi_objects.process_group import ProcessGroup, ProcessGroupWithPorts
from nifi_objects.connection import Connection
from nifi_objects.remote_process_groups import RemoteProcessGroup

class NifiService:
    def __init__(self, base_url: str, username: str, password: str, verify_ssl: bool = True):
        self.base_url = base_url.rstrip('/')
        self.username = username
        self.password = password
        self.verify_ssl = verify_ssl
        self.token = None

        self.process_group_handler = ProcessGroupHandler(self.nifi_request, self.validate_response_status)
        self.diagnostics_handler = DiagnosticsHandler(self.nifi_request, self.validate_response_status)
        self.funnel_handler = FunnelHandler(self.nifi_request, self.validate_response_status)
        self.ports_handler = PortsHandler(self.nifi_request, self.validate_response_status)
        self.connection_handler = ConnectionHandler(self.nifi_request, self.validate_response_status)
        self.remote_process_group_handler = RemoteProcessGroupHandler(self.nifi_request, self.validate_response_status)
        self.parameter_context_handler = ParameterContextHandler(self.nifi_request, self.validate_response_status)

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

    def _get_token(self) -> str:
        response = requests.post(f'{self.base_url}/access/token', data={"username": self.username, "password": self.password}, verify=self.verify_ssl)
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
        if res.status_code == 401:
            if retry_count <= 0:
                raise UnauthorizedError('Unauthorized - check username and password')
            self.token = self._get_token()
            return self.nifi_request(method, url, json=json, data=data, params=params, retry_count=retry_count - 1)
        return res

    def is_nifi_connection_alive(self):
        return self.diagnostics_handler.is_nifi_connection_alive()

    def get_root_id(self):
        return self.process_group_handler.get_root_id()

    def create_process_group(self, process_group:ProcessGroup, father_id:str):
        return self.process_group_handler.create_process_group(process_group, father_id)

    def update_process_group(self, process_group:ProcessGroup, father_id):
        return self.process_group_handler.update_process_group(process_group, father_id)

    def get_process_group(self, pg_id:str):
        return self.process_group_handler.get_process_group(pg_id)

    def get_all_process_groups(self, father_id):
        return self.process_group_handler.get_all_process_groups(father_id)

    def create_funnel(self, funnel:Funnel, father_id):
        return self.funnel_handler.create_funnel(funnel, father_id)

    def create_port(self, port:Port, father_id:str):
        return self.ports_handler.create_port(port, father_id)

    def get_all_ports(self, port_type: PortType, father_id: str):
        return self.ports_handler.get_all_ports(port_type, father_id)

    def create_connection(self, connection: Connection, father_id):
        return self.connection_handler.create_connection(connection, father_id)

    def create_parameter_context(self, parameter_context_group:ParameterContext):
        return self.parameter_context_handler.create_parameter_context(parameter_context_group)

    def update_parameter_context(self, context_id:str, parameter_context:ParameterContext):
        return self.parameter_context_handler.update_parameter_context(context_id, parameter_context)

    def create_remote_process_group(self, remote_pg:RemoteProcessGroup, father_id:str):
        return self.remote_process_group_handler.create_remote_process_group(remote_pg, father_id)

    def create_pg_with_ports(self, process_group_with_ports:ProcessGroupWithPorts, father_id):
        new_process_group = self.create_process_group(process_group_with_ports.process_group, father_id)
        input_port = self.create_port(process_group_with_ports.input_port, new_process_group["id"])
        output_port = self.create_port(process_group_with_ports.output_port, new_process_group["id"])
        updated_process_group = self.get_process_group(new_process_group["id"])
        return {'process_group': updated_process_group, 'input_port': input_port, 'output_port': output_port}