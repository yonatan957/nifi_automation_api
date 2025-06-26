from pydantic import BaseModel
from typing import Optional
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

class ProcessGroupWithPorts(BaseModel):
    process_group: ProcessGroup
    input_port: InputPort
    output_port: OutPutPort