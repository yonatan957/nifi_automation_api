from nifi_objects.general_objects import NifiObject, Component, Connectable
from typing import Optional, List

class Connection(NifiObject):
    class ConnectionComponent(Component):
        source: Optional[Connectable] = None
        destination: Optional[Connectable] = None

    component: Optional[ConnectionComponent] = None