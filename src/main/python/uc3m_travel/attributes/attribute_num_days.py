"""NumDays Attribute"""
from uc3m_travel.attributes import Attribute
from uc3m_travel.hotel_management_exception import HotelManagementException
# pylint: disable=useless-parent-delegation

class NumDays(Attribute):
    """NumDays Attribute"""
    def __init__(self, num_days):
        super().__init__()
        self._attr_value = self._validate(num_days)
    def _validate(self, attr_value):
        """validates the number of days"""
        try:
            days = int(attr_value)
        except ValueError as ex:
            raise HotelManagementException("Invalid num_days datatype") from ex
        if days < 1 or days > 10:
            raise HotelManagementException("Num_days should be in the range 1-10")
        return attr_value
