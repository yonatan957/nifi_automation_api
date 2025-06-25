from pydantic import BaseModel
from nifi_objects.general_objects import Revision, Position

class Funnel(BaseModel):

    id: str
    position: Position
    revision: Revision