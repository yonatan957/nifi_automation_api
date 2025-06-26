from pydantic import BaseModel
from typing import Optional
from nifi_objects.general_objects import Revision, Position
class ProcessGroup(BaseModel):
    class Component(BaseModel):
        id: Optional[str]
        name: Optional[str]
        comments: Optional[str]
        position: Optional[str]

    revision: Optional[Revision]
    id: Optional[str]
    component: Optional[Component]