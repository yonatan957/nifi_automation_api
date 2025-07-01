from pydantic import BaseModel
from typing import Optional, List
from nifi_services.types import ConnectableType
class Position(BaseModel):
    x: Optional[float] = None
    y: Optional[float] = None

class Revision(BaseModel):
    version: Optional[float] = None

class Component(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    comments: Optional[str] = None
    position: Optional[Position] = None

class Connectable(BaseModel):
    id: Optional[str] = None
    type: Optional[ConnectableType] = None
    name: Optional[str] = None
    groupId: Optional[str] = None

class NifiObject(BaseModel):
    id: Optional[str] = None
    component: Optional[Component] = None
    revision: Optional[Revision] = None