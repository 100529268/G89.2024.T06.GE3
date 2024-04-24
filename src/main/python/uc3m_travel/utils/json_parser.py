"""Json parser Class Method"""
import json
from ..attributes import IDCard, Localizer
from ..hotel_management_exception import HotelManagementException


class JsonParser:
    """JSON parser class"""

    def __init__(self, file_path: str):
        self.file_path = file_path

    def read_input_from_file(self):
        """Reads JSON input from a file and returns extracted data"""
        try:
            with open(self.file_path, "r", encoding="utf-8", newline="") as file:
                input_list = json.load(file)
        except FileNotFoundError as ex:
            raise HotelManagementException("Error: file input not found") from ex
        except json.JSONDecodeError as ex:
            raise HotelManagementException("JSON Decode Error - Wrong JSON Format") from ex

        try:
            my_id_card, my_localizer = self.validate_parsed_data(input_list)
        except KeyError as e:
            raise HotelManagementException("Error - Invalid Key in JSON") from e
        return my_id_card, my_localizer

    def validate_parsed_data(self, input_list):
        """validates the parsed data"""
        my_localizer = input_list["Localizer"]
        my_id_card = input_list["IdCard"]
        # Validate IdCard and Localizer
        IDCard(my_id_card)
        Localizer(my_localizer)
        return my_id_card, my_localizer
