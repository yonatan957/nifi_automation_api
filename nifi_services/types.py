from enum import Enum
from typing import Dict, Any, Optional, TypedDict

GenericDict = Optional[Dict[Any, Any]]

class Request_Type(Enum):
    GET = "GET"
    POST = "POST"
    DELETE = "DELETE"
    PUT = "PUT"

class ConnectableType(str, Enum):
    PROCESSOR = "PROCESSOR"
    REMOTE_INPUT_PORT = "REMOTE_INPUT_PORT"
    REMOTE_OUTPUT_PORT = "REMOTE_OUTPUT_PORT"
    INPUT_PORT = "INPUT_PORT"
    OUTPUT_PORT = "OUTPUT_PORT"
    FUNNEL = "FUNNEL"

class PortType(str, Enum):
    INPUT_PORT = "INPUT-PORT"
    OUTPUT_PORT = "OUTPUT-PORT"