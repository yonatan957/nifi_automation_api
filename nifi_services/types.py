from enum import Enum
from typing import Dict, Any, Optional, TypedDict

GenericDict = Optional[Dict[str, any]]

class Request_Type(Enum):
    GET = "GET"
    POST = "POST"
    DELETE = "DELETE"
    PUT = "PUT"