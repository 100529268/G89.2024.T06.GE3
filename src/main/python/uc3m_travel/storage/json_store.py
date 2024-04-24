"""Module for the hotel manager"""
import json
from uc3m_travel.hotel_management_exception import HotelManagementException


class JsonStore:

    def __init__(self, file_name):
        self._file_name = file_name
        self._data_list = []

    def save_list_to_file(self):
        try:
            with open(self._file_name, "w", encoding="utf-8", newline="") as file:
                json.dump(self._data_list, file, indent=2)
        except FileNotFoundError as ex:
            raise HotelManagementException("Wrong file  or file path") from ex

    def load_list_from_file(self, msg):
        try:
            with open(self._file_name, "r", encoding="utf-8", newline="") as file:
                self._data_list = json.load(file)
        except FileNotFoundError as ex:
            if not msg == "pass error":
                raise HotelManagementException(msg) from ex
            self._data_list = []
        except json.JSONDecodeError as ex:
            raise HotelManagementException("JSON Decode Error - Wrong JSON Format") from ex

    def add_item(self, item):
        if not type(item) == dict: item = item.__dict__
        self._data_list.append(item)
        self.save_list_to_file()

    def find_item(self, key, value, msg):
        """finds an item in a storage"""
        self.load_list_from_file(msg)
        for item in self._data_list:
            if item[key] == value:
                return item
        return None
