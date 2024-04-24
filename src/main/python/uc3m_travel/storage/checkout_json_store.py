"""Module for the hotel manager"""
from datetime import datetime

from uc3m_travel.hotel_management_exception import HotelManagementException
from uc3m_travel.hotel_management_config import JSON_FILES_PATH
from uc3m_travel.storage.json_store import JsonStore


class CheckoutJsonStore(JsonStore):
    _file_name = JSON_FILES_PATH + "store_check_out.json"

    def __init__(self):
        super().__init__(self._file_name)
    def add_stay(self, room_key):
        # checks for duplicate reservations
        if super().find_item("room_key", room_key, "pass error"):
            raise HotelManagementException("Guest is already out")

        room_checkout = {"room_key": room_key, "checkout_time": datetime.timestamp(datetime.utcnow())}
        super().add_item(room_checkout)
