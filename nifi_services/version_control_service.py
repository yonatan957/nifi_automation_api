from nifi_services.nifi_service import NifiService
from nifi_services.nifi_registry_service import NifiRegistryService
from nifi_objects.parameter_context import ParameterContext
from nifi_objects.process_group import ProcessGroup
from nifi_objects.connection_details import ConnectionDetails
from utils.consts import REGISTRY_ID, BUCKET_ID
from utils.logger import logger
class VersionControlService:
    def __init__(self, nifi_service:NifiService, nifi_registry_service:NifiRegistryService):
        self.nifi_service = nifi_service
        self.nifi_registry_service = nifi_registry_service

    def create_pg_from_version_control(self, connection_details:ConnectionDetails):
        parameter_context: ParameterContext = ParameterContext(**self.create_parameter_context_to_version_control(
            connection_details.host,
            connection_details.queue,
            connection_details.username,
            connection_details.password,
            connection_details.port
        ))
        new_parameter_context = self.nifi_service.create_parameter_context(parameter_context)

        root_id = self.nifi_service.get_root_id()

        version_control = self.nifi_registry_service.get_version_control()

        process_group = self.create_process_group(new_parameter_context, version_control)
        new_process_group = self.nifi_service.create_process_group(process_group, root_id)
        small_new_process_group = self.nifi_service.get_process_group(new_process_group['component']['id'])
        small_new_process_group['parameterContext'] = small_new_process_group["component"]["parameterContext"] = {
            "id": new_parameter_context['id'],
            "name": new_parameter_context["component"]['name'],
            'component': {
                "id": new_parameter_context["id"]
            }
        }
        update_pg = ProcessGroup(**small_new_process_group)
        result = self.nifi_service.update_process_group(update_pg)
        return result

    def create_process_group(self, parameter_context, version_control):
        return ProcessGroup(**{
            'revision': {
                'version' : version_control['revision']['version']
            },
            'parameterContext': {
                'id': parameter_context['id'],
                'component': {
                    'id': parameter_context['id'],
                    'name': parameter_context['component']['name']
                }
            },
            'component':{
                'name': 'rabbit_trail',
                'position': {
                    'x': 250,
                    'y': 250
                },
                'versionControlInformation': {
                    'registryId': REGISTRY_ID,
                    'bucketName': version_control['bucketName'],
                    'bucketId': BUCKET_ID,
                    'flowId': version_control['identifier'],
                    'version': version_control['versionCount']
                }
            }
        })
    def create_parameter_context_to_version_control(self, hostname, queue, username, password, port):
        return {
          "revision":{
              "version": 0,
          },
          "component": {
            "name": "parameter_context_new",
            "parameters": [
              {
                "canWrite": True,
                "parameter": {
                  "name": "queue",
                  "description": "Queue name",
                  "sensitive": False,
                  "value": str(queue)
                }
              },
              {
                "canWrite": True,
                "parameter": {
                  "name": "username",
                  "description": "Username for connection",
                  "sensitive": False,
                  "value": username
                }
              },
              {
                "canWrite": True,
                "parameter": {
                  "name": "password",
                  "description": "Password for connection",
                  "sensitive": True,
                  "value": password
                }
              },
              {
                "canWrite": True,
                "parameter": {
                  "name": "hostname",
                  "description": "Host name",
                  "sensitive": False,
                  "value": hostname
                }
              },
              {
                "canWrite": True,
                "parameter": {
                  "name": "port",
                  "description": "Port number",
                  "sensitive": False,
                  "value": str(port)
                }
              }
            ]
          }
        }