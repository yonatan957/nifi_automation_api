from nifi_objects.general_objects import  NifiObject, Component
from nifi_objects.port import InputPort, OutPutPort
from typing import Optional, List
from pydantic import BaseModel

class ParameterContextReference(BaseModel):
    class Permissions(BaseModel):
        canRead: Optional[bool] = True,
        canWrite: Optional[bool] = True
    class Component(BaseModel):
        id: Optional[str] = None
        name: Optional[str] = None
    id: Optional[str] = None
    component: Component

class VersionControlInformation(BaseModel):
    registryId: Optional[str] = None
    bucketName: Optional[str] = None
    bucketId: Optional[str] = None
    flowId: Optional[str] = None
    version: Optional[int] = None

class ProcessGroup(NifiObject):
    class Component(Component):
        versionControlInformation: Optional[VersionControlInformation] = None
        parameterContext: Optional[ParameterContextReference] = None
    component: Optional[Component] = None
    parameterContext: Optional[ParameterContextReference] = None

class ProcessGroupWithPorts(BaseModel):
    process_group: ProcessGroup
    input_port: InputPort
    output_port: OutPutPort