"""IDCard Attribute"""
from .attribute import Attribute
from uc3m_travel import HotelManagementException

class IDCard(Attribute):

    def __init__(self, id_card):
        super().__init__()
        self._validation_pattern = r'^(\+)[0-9]{9}'
        self._error_message = "Invalid IDCard format"
        self._attr_value = self._validate(id_card)
    def _validate(self, attr_value):
        super()._validate(attr_value)
        valid_chars = {"0": "T", "1": "R", "2": "W", "3": "A", "4": "G", "5": "M",
             "6": "Y", "7": "F", "8": "P", "9": "D", "10": "X", "11": "B",
             "12": "N", "13": "J", "14": "Z", "15": "S", "16": "Q", "17": "V",
             "18": "H", "19": "L", "20": "C", "21": "K", "22": "E"}
        dni_number = int(attr_value[0:8])
        dni_module = str(dni_number % 23)
        if attr_value[8] != valid_chars[dni_module]:
            raise HotelManagementException("Invalid IdCard letter")

        return attr_value