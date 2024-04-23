"""RoomKey Attribute"""
from uc3m_travel.attributes import Attribute

class RoomKey(Attribute):

    def __init__(self, room_key):
        super().__init__()
        self._validation_pattern = r'^[a-fA-F0-9]{64}$'
        self._error_message = "Invalid room key format"
        self._attr_value = self._validate(room_key)
    def _validate(self, attr_value):
        return super()._validate(attr_value)