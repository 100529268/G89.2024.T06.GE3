import hashlib
import json
from uc3m_travel.hotel_management_exception import HotelManagementException



class JsonStore():
    """Json Store Class"""

    _data_list = []
    _file_name = ""

    def __init__(self):
        self.file_path = self._file_name
        self.data_list = self._data_list

    def save_reservation(self, reservation_data):
        """Saves reservation data to the JSON store"""
        _file_name = "store_reservation.json"
        self.file_path = self.construct_file_path(_file_name)

        try:
            with open(self.file_path, "r", encoding="utf-8", newline="") as file:
                self.data_list = json.load(file)
                print(self.file_path)
        except FileNotFoundError:
            self.data_list = []
        except json.JSONDecodeError as ex:
            raise HotelManagementException("JSON Decode Error - Wrong JSON Format") from ex

        for item in self.data_list:
            if reservation_data.get("_HotelReservation__localizer") == item["_HotelReservation__localizer"]:
                raise HotelManagementException("Reservation already exists")
            if reservation_data.get("_HotelReservation__id_card") == item["_HotelReservation__id_card"]:
                print("error2!!!!!!!!!!")
                raise HotelManagementException("This ID card has another reservation")

        self.data_list.append(reservation_data)

        try:
            with open(self.file_path, "w", encoding="utf-8", newline="") as file:
                json.dump(self.data_list, file, indent=2)
        except FileNotFoundError as ex:
            raise HotelManagementException("Wrong file  or file path") from ex

    # def save_checkin(self, checkin_data):
    #     """Saves checkin data to the JSON store"""
    #     _file_name = "store_checkin.json"
    #     self.file_path = self.construct_file_path(_file_name)
    #
    #     try:
    #         with open(self.file_path, "r", encoding="utf-8", newline="") as file:
    #             self.data_list = json.load(file)
    #             print(self.file_path)
    #     except FileNotFoundError:
    #         self.data_list = []
    #     except json.JSONDecodeError as ex:
    #         raise HotelManagementException("JSON Decode Error - Wrong JSON Format") from ex
    #
    #     for item in self.data_list:
    #         if checkin_data.get("_HotelReservation__localizer") == item["_HotelReservation__localizer"]:
    #             raise HotelManagementException("Reservation already exists")
    #         if checkin_data.get("_HotelReservation__id_card") == item["_HotelReservation__id_card"]:
    #             print("error2!!!!!!!!!!")
    #             raise HotelManagementException("This ID card has another reservation")
    #
    #     self.data_list.append(checkin_data)
    #
    #     try:
    #         with open(self.file_path, "w", encoding="utf-8", newline="") as file:
    #             json.dump(self.data_list, file, indent=2)
    #     except FileNotFoundError as ex:
    #         raise HotelManagementException("Wrong file  or file path") from ex
    #
    # def save_checkout(self, checkout_data):
    #     """Saves checkin data to the JSON store"""
    #     _file_name = "store_checkout.json"
    #     self.file_path = self.construct_file_path(_file_name)
    #
    #     try:
    #         with open(self.file_path, "r", encoding="utf-8", newline="") as file:
    #             self.data_list = json.load(file)
    #             print(self.file_path)
    #     except FileNotFoundError:
    #         self.data_list = []
    #     except json.JSONDecodeError as ex:
    #         raise HotelManagementException("JSON Decode Error - Wrong JSON Format") from ex
    #
    #     for item in self.data_list:
    #         if checkout_data.get("_HotelReservation__localizer") == item["_HotelReservation__localizer"]:
    #             raise HotelManagementException("Reservation already exists")
    #         if checkout_data.get("_HotelReservation__id_card") == item["_HotelReservation__id_card"]:
    #             print("error2!!!!!!!!!!")
    #             raise HotelManagementException("This ID card has another reservation")
    #
    #     self.data_list.append(checkout_data)
    #
    #     try:
    #         with open(self.file_path, "w", encoding="utf-8", newline="") as file:
    #             json.dump(self.data_list, file, indent=2)
    #     except FileNotFoundError as ex:
    #         raise HotelManagementException("Wrong file  or file path") from ex
    #


    def save_list_to_file(self):
        """Saves list to json file"""
        with open(self.file_path, "w", encoding="utf-8", newline="") as file:
            json.dump(self._data_list, file, indent=2)

    def load_list_from_file(self):
        """Loads list from json file"""
        try:
            with open(self.file_path, "r", encoding="utf-8", newline="") as file:
                _data_list = json.load(file)
                print(self.file_path)
        except FileNotFoundError:
            _data_list = []
        except json.JSONDecodeError as ex:
            raise HotelManagementException("JSON Decode Error - Wrong JSON Format") from ex
    def add_item(self, item):
        """Adds item to json store"""
        self.load_list_from_file()
        self._data_list.append(item)
        self.save_list_to_file()
    def find_item(self, key, value):
        """finds an item in the store"""
        self.load_list_from_file()
        for item in self._data_list:
            if item[key] == value:
                return item
        return None

    def construct_file_path(self, file_name) -> str:
        """changes file path depending on method """
        from uc3m_travel import JSON_FILES_PATH
        return JSON_FILES_PATH + file_name

    # @property
    # def hash(self):
    #     """Returns the hash of the store for checking modifications"""
    #     self.load_list_from_file()
    #     return hashlib.md5(self._data_list.encode('utf-8')).hexdigest()
