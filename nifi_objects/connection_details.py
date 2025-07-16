from pydantic import BaseModel
from typing import Optional, List

class ConnectionDetails(BaseModel):
    queue: Optional[float] = None
    host: Optional[str] = 'localhost'
    port: Optional[float] = 15672
    username: Optional[str] = None
    password: Optional[str] = None