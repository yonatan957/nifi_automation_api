from pydantic import BaseModel

class ProcessGroup(BaseModel):
    class Revision(BaseModel):
        version: int

    class Component(BaseModel):
        class Position(BaseModel):
            x: float
            y: float

        id: str
        name: str
        comments: str
        position: Position

    revision: Revision
    id: str
    component: Component