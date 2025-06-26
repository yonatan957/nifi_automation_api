from pydantic import BaseModel
from nifi_objects.general_objects import Revision, Position
from typing import Optional
class Port(BaseModel):
    revision: Optional[Revision] = None
    id: Optional[str] = None
    position: Optional[Position] = None

class InputPort(Port):
    pass

class OutPUtPort(Port):
    pass