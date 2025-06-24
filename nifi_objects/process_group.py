from pydantic import BaseModel

class Process_Group(BaseModel):
    revision: Revision

class Revision(BaseModel):
    version: int