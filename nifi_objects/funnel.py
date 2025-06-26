from pydantic import BaseModel
from nifi_objects.general_objects import Revision, Position
from typing import Optional

class Funnel(BaseModel):
    class Component(BaseModel):
        position:Optional[Position] = None
        id: Optional[str] = None
    id: Optional[str] = None
    component: Optional[Component] = None
    revision: Optional[Revision] = None