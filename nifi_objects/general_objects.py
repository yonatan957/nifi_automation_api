from pydantic import BaseModel
from typing import Optional
class Position(BaseModel):
    x: Optional[float] = None
    y: Optional[float] = None


class Revision(BaseModel):
    version: Optional[float] = None