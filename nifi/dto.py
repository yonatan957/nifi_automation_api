from enum import Enum
from typing import Dict, Any, Optional, TypedDict
Parameters_Type = Optional[Dict[str, any]]

def create_pg_payload(name:str, x_position:float= 0.0, y_position:float= 0.0) -> Parameters_Type :
    return {
        "revision": {"version":0},
        "component": {
            "name": name,
            "position": {"x":x_position, "y":y_position}
        }
    }

def create_funnel_payload() -> Parameters_Type:
    return {
        "revision":{"version":0},
        "component": {
            "position": {"x":0.0, "y":0.0}
        }
    }
class ConnectionResult(TypedDict):
    succeeded: bool
    message: str

class Request_Type(Enum):
    GET = "GET"
    POST = "POST"
    DELETE = "DELETE"
    PUT = "PUT"