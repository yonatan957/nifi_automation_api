from enum import Enum
from typing import Dict, Any, Optional, TypedDict

GenericDict = Optional[Dict[Any, Any]]

class Request_Type(Enum):
    GET = "GET"
    POST = "POST"
    DELETE = "DELETE"
    PUT = "PUT"