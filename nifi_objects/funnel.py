from pydantic import BaseModel

class Funnel(BaseModel):
    class Revision(BaseModel):
        version: int

    class Position(BaseModel):
        x: int
        y: int

    id: str
    position: Position
    revision: Revision