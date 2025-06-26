from pydantic import BaseModel
from typing import Optional
from nifi_objects.general_objects import Revision, Position
class ProcessGroup(BaseModel):
    class Component(BaseModel):
        id: Optional[str] = None
        name: Optional[str] = None
        comments: Optional[str] = None
        position: Optional[Position] = None

    revision: Optional[Revision] = None
    id: Optional[str] = None
    component: Optional[Component] = None