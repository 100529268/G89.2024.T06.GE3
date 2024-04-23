"""Localizer Attribute"""
from uc3m_travel.attributes import Attribute

class Localizer(Attribute):

    def __init__(self, localizer):
        super().__init__()
        self._validation_pattern = r'^[a-fA-F0-9]{32}$'
        self._error_message = "Invalid localizer"
        self._attr_value = self._validate(localizer)
    def _validate(self, attr_value):
        return super()._validate(attr_value)