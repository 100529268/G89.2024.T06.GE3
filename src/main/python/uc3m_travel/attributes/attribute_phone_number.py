"""PhoneNumber Attribute"""
from uc3m_travel.attributes import Attribute
# pylint: disable=useless-parent-delegation

class PhoneNumber(Attribute):
    """PhoneNumber Attribute"""
    def __init__(self, phone_number):
        super().__init__()
        self._validation_pattern = r'^(\+)[0-9]{9}'
        self._error_message = "Invalid phone number format"
        self._attr_value = self._validate(phone_number)
    def _validate(self, attr_value):
        return super()._validate(attr_value)
