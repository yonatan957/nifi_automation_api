from enum import Enum
from typing import Dict, Any, Optional
def create_pg_payload(name:str, x_position:float= 0.0, y_position:float= 0.0) -> json :
    return {
        "revision": {"version":0},
        "component": {
            "name": name,
            "position": {x_position, y_position}
        }
    }

Parameters_Type = Optional[Dict[str, any]]

class Request_Type(Enum):
    GET = "GET"
    POST = "POST"
    DELETE = "DELETE"
    PUT = "PUT"