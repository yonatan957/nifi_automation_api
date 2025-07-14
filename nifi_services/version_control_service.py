from nifi_services.nifi_service import NifiService
from nifi_services.nifi_registry_service import NifiRegistryService

class VersionControlService:
    def __init__(self, nifi_service:NifiService, nifi_registry_service:NifiRegistryService):
        self.nifi_service = nifi_service
        self.nifi_registry_service = nifi_registry_service


    def create_pg_from_version_control(self):
        return