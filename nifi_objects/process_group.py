from general_objects import  NifiObject, Component
from typing import Optional, List
from pydantic import BaseModel

class ParameterContextReference(BaseModel):
    id: Optional[str] = None

class ProcessGroup(NifiObject):
    class Component(Component):
        parameterContext: Optional[ParameterContextReference] = None
    component: Optional[Component] = None


class ProcessGroupWithPorts(BaseModel):
    process_group: ProcessGroup
    input_port: InputPort
    output_port: OutPutPort