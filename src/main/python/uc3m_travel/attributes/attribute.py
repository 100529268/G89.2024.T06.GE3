"""Attribute Class for Reservation Data"""
import re
from uc3m_travel import HotelManagementException

class Attribute:

    def __init__(self):
        self._attr_value = ''
        self._validation_pattern = ''
        self._error_message = ''

    def _validate(self, attr_value):
        myregex = re.compile(self._validation_pattern)
        regex_matches = myregex.fullmatch(attr_value)
        if not regex_matches:
            raise HotelManagementException(self._error_message)
        return attr_value

    @property
    def value(self):
        """returns attr_value"""
        return self._attr_value

    @value.setter
    def value(self, attr_value):
        """sets attr_value"""

        self._attr_value = self._validate(attr_value)