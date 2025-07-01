from pydantic import BaseModel
from typing import Optional, List
from nifi_services.types import ConnectableType
class Position(BaseModel):
    x: Optional[float] = None
    y: Optional[float] = None


class Revision(BaseModel):
    version: Optional[float] = None

class Component(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    comments: Optional[str] = None
    position: Optional[Position] = None

class Connectable(BaseModel):
    id: Optional[str] = None
    type: Optional[ConnectableType] = None
    name: Optional[str] = None
    groupId: Optional[str] = None

class NifiObject(BaseModel):
    id: Optional[str] = None
    component: Optional[Component] = None
    revision: Optional[Revision] = None

class Funnel(NifiObject):
    pass

class Port(NifiObject):
    pass

class InputPort(Port):
    pass

class OutPutPort(Port):
    pass

class ProcessGroup(NifiObject):
    pass


class ParameterDto(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    sensitive: Optional[bool] = None
    value: Optional[str] = None

class Parameter(BaseModel):
    canWrite: Optional[bool] = None
    parameter: Optional[ParameterDto] = None

class ParameterContext(NifiObject):
    class Component(Component):
        parameters: Optional[List[Parameter]] = None
        id: Optional[str] = None
    component: Optional[Component] = None

class RemoteProcessGroup(NifiObject):
    class RPG_Component(Component):
        targetUri: Optional[str] = None
    component: RPG_Component
    uri: Optional[str] = None
    pass

class Connection(NifiObject):
    class ConnectionComponent(Component):
        source: Optional[Connectable] = None
        destination: Optional[Connectable] = None

    component: Optional[ConnectionComponent] = None

class ProcessGroupWithPorts(BaseModel):
    process_group: ProcessGroup
    input_port: InputPort
    output_port: OutPutPort