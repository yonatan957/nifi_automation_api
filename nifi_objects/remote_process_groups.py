from nifi_objects.general_objects import NifiObject, Component, Optional
class RemoteProcessGroup(NifiObject):
    class RPG_Component(Component):
        targetUri: Optional[str] = None
    component: RPG_Component
    uri: Optional[str] = None
    pass