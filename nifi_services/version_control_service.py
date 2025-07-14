from nifi_services.nifi_service import NifiService
from nifi_services.nifi_registry_service import NifiRegistryService
from nifi_objects.parameter_context import ParameterContext
from nifi_objects.connection_details import ConnectionDetails
class VersionControlService:
    def __init__(self, nifi_service:NifiService, nifi_registry_service:NifiRegistryService):
        self.nifi_service = nifi_service
        self.nifi_registry_service = nifi_registry_service

    def create_pg_from_version_control(self, connection_details:ConnectionDetails):
        # create parameter context, with the values
        parameter_context: ParameterContext = ParameterContext(**self.create_parameter_context_to_version_control(
            connection_details.host,
            connection_details.queue,
            connection_details.username,
            connection_details.password,
            connection_details.port
        ))
        new_parameter_context = self.nifi_service.create_parameter_context(parameter_context)

        # get the id of the root process group
        root_id = self.nifi_service.get_root_id()

        # get the id of the version control and id


        # create process group with this parameter context and with the version control
        return

    def create_parameter_context_to_version_control(self, hostname, queue, username, password, port):
        return {
          "component": {
            "id": "example-context-id",
            "parameters": [
              {
                "canWrite": true,
                "parameter": {
                  "name": "queue",
                  "description": "Queue name",
                  "sensitive": false,
                  "value": str(queue)
                }
              },
              {
                "canWrite": true,
                "parameter": {
                  "name": "username",
                  "description": "Username for connection",
                  "sensitive": false,
                  "value": username
                }
              },
              {
                "canWrite": true,
                "parameter": {
                  "name": "password",
                  "description": "Password for connection",
                  "sensitive": true,
                  "value": password
                }
              },
              {
                "canWrite": true,
                "parameter": {
                  "name": "hostname",
                  "description": "Host name",
                  "sensitive": false,
                  "value": hostname
                }
              },
              {
                "canWrite": true,
                "parameter": {
                  "name": "port",
                  "description": "Port number",
                  "sensitive": false,
                  "value": str(port)
                }
              }
            ]
          }
        }
