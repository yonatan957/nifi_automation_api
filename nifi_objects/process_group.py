from pydantic import BaseModel

class Revision(BaseModel):
    version: int

class Position(BaseModel):
    x: float
    y: float

class Component(BaseModel):
    id: str
    name: str
    comments: str
    position: Position

class Process_Group(BaseModel):
    revision: Revision
    id: str
    component: Component
