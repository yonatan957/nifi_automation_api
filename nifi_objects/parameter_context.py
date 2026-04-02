from pydantic import BaseModel
from general_objects import Component, NifiObject

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