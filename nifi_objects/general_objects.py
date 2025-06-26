from pydantic import BaseModel
from typing import Optional
class Position(BaseModel):
    x: Optional[float]
    y: Optional[float]


class Revision(BaseModel):
    version: Optional[float]