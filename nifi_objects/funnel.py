from pydantic import BaseModel
from nifi_objects.general_objects import Revision, Position
from typing import Optional

class Funnel(BaseModel):

    id: Optional[str]
    position: Optional[Position]
    revision: Optional[Revision]