"""Module for the hotel manager"""
import re
import json
from datetime import datetime
from uc3m_travel.hotel_management_exception import HotelManagementException
from uc3m_travel.hotel_reservation import HotelReservation
from uc3m_travel.hotel_stay import HotelStay
from uc3m_travel.hotel_management_config import JSON_FILES_PATH
from freezegun import freeze_time
from uc3m_travel.storage.json_store import JsonStore


class StayJsonStore(JsonStore):
    _file_name = JSON_FILES_PATH + "store_check_in.json"

    def add_item(self, item):
        reservation_found = self.find_item(item.localizer, "_HotelReservation__localizer")

        if reservation_found:
            raise HotelManagementException("Store already exists")
        super.add_item(item)

    def save_reservation(self, reservation_data):
        super.file_name = self._file_name
        self.add_item(reservation_data)
        super.save_list_to_file()
