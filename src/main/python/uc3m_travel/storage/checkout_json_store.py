from uc3m_travel.storage.json_store import JsonStore
from uc3m_travel.hotel_management_config import JSON_FILES_PATH


class CheckoutJsonStore(JsonStore):
    """Checkout JSON store singleton class"""

    def __init__(self):
        pass

    # def save_checkout(self, checkout_data):
    #     """Saves checkout data to JSON store"""
    #     self.save_data(checkout_data)
    #
    # def add_item(self, item):
    #     from uc3m_travel.hotel_management_exception import HotelManagementException
    #     room_key_found = self.find_item(item["room_key"], "room_key")
    #     if room_key_found:
    #         raise HotelManagementException("Room key already exists in checkout")
    #     super().save_data(item)
