"""CreditCard Attribute"""
from uc3m_travel.hotel_management_exception import HotelManagementException
from uc3m_travel.attributes import Attribute
# pylint: disable=useless-parent-delegation

class CreditCard(Attribute):
    """CreditCard Attribute"""

    def __init__(self, credit_card):
        super().__init__()
        self._validation_pattern = r'^[0-9]{16}'
        self._error_message = "Invalid credit card format"
        self._attr_value = self._validate(credit_card)

    def _validate(self, attr_value):
        super()._validate(attr_value)

        def digits_of(n):
            return [int(DIGITS) for DIGITS in str(n)]

        digits = digits_of(attr_value)
        odd_digits = digits[-1::-2]
        even_digits = digits[-2::-2]
        checksum = 0
        checksum += sum(odd_digits)
        for d in even_digits:
            checksum += sum(digits_of(d * 2))
        if not checksum % 10 == 0:
            raise HotelManagementException("Invalid credit card number (not luhn)")

        return attr_value
