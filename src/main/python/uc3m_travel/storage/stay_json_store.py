"""Module for the hotel manager"""

from uc3m_travel.hotel_management_exception import HotelManagementException
from uc3m_travel.hotel_management_config import JSON_FILES_PATH
from uc3m_travel.storage.json_store import JsonStore
# pylint: disable=invalid-name

class StayJsonStore(JsonStore):
    """Stays storage class"""
    class __StayJsonStore(JsonStore):
        """Stays storage class"""
        _file_name = JSON_FILES_PATH + "store_check_in.json"


        def __init__(self):
            """Constructor"""
            super().__init__(self._file_name)

        def find_stay(self, room_key):
            """Find stay from room key"""
            return super().find_item(
                "_HotelStay__room_key", room_key, "Error: store checkin not found")

        def add_stay(self, stay):
            """ adds stay to hotel """
            # checks for duplicate stays
            if super().find_item("_HotelStay__room_key", stay.room_key, "pass error"):
                raise HotelManagementException("Check-in  ya realizado")

            super().add_item(stay)

    __instance = None

    def __new__(cls):
        """create a new instance of the class"""
        if StayJsonStore.__instance is None:
            StayJsonStore.__instance = StayJsonStore.__StayJsonStore()
        return StayJsonStore.__instance
