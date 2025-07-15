from nifi_objects.general_objects import  NifiObject, Component
from nifi_objects.port import InputPort, OutPutPort
from typing import Optional, List
from pydantic import BaseModel

class ParameterContextReference(BaseModel):
    id: Optional[str] = None

class VersionControlInformation(BaseModel):
    registryId: Optional[str] = None
    bucketName: Optional[str] = None
    bucketId: Optional[str] = None
    flowId: Optional[str] = None
    version: Optional[int] = None

class ProcessGroup(NifiObject):
    class Component(Component):
        parameterContext: Optional[ParameterContextReference] = None
        versionControlInformation: Optional[VersionControlInformation] = None
    component: Optional[Component] = None


class ProcessGroupWithPorts(BaseModel):
    process_group: ProcessGroup
    input_port: InputPort
    output_port: OutPutPort