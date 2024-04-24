"""RoomType Attribute"""
from uc3m_travel.attributes import Attribute

class RoomType(Attribute):
    """RoomType Attribute"""
    def __init__(self, room_type):
        super().__init__()
        self._validation_pattern = r'(SINGLE|DOUBLE|SUITE)'
        self._error_message = "Invalid room-type value"
        self._attr_value = self._validate(room_type)
    def _validate(self, attr_value):
        return super()._validate(attr_value)
