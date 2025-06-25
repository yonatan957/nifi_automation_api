from pydantic import BaseModel

class Position(BaseModel):
    x: float
    y: float


class Revision(BaseModel):
    version: int