"""Module for the hotel manager"""
import re
import json
from datetime import datetime
from uc3m_travel.hotel_management_exception import HotelManagementException
from uc3m_travel.hotel_reservation import HotelReservation
from uc3m_travel.hotel_stay import HotelStay
from uc3m_travel.hotel_management_config import JSON_FILES_PATH
from freezegun import freeze_time

class JsonStore():
    _data_list = []
    _file_name = ""

    def __init__(self):
        pass

    def save_list_to_file(self):
        try:
            with open(self._file_name, "w", encoding="utf-8", newline="") as file:
                json.dump(self._data_list, file, indent=2)
        except FileNotFoundError as ex:
            raise HotelManagementException("Wrong file  or file path") from ex

    def load_list_from_file(self):
        try:
            with open(self._file_name, "r", encoding="utf-8", newline="") as file:
                self._data_list = json.load(file)
        except FileNotFoundError as ex:
            raise HotelManagementException("Error: store reservation not found") from ex
        except json.JSONDecodeError as ex:
            raise HotelManagementException("JSON Decode Error - Wrong JSON Format") from ex

    def add_item(self, item):
        self.load_list_from_file(self._file_name)
        self._data_list.append(item.__dict__)

    def find_item(self, key, value):
        """finds an item in a storage"""
        self.load_list_from_file()
        for item in self._data_list:
            if item[key] == value:
                return item
        return None

    @_file_name.setter
    def id_card(self, file_name):
        self._file_name = file_name

    @property
    def data_list(self):
        """Returns _data_list property"""
        return self._data_list

    def save_checkin(self, checkin_data):
        pass

    def save_checkout(self, checkout_data):
        pass
