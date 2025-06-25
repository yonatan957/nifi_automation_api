from pydantic import BaseModel
from nifi_objects.general_objects import Revision, Position
class ProcessGroup(BaseModel):
    class Component(BaseModel):
        id: str
        name: str
        comments: str
        position: Position

    revision: Revision
    id: str
    component: Component