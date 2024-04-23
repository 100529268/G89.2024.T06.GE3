from uc3m_travel.storage.json_store import JsonStore



class ReservationJsonStore(JsonStore):
    """Reservation JSON store singleton class"""

    def __init__(self):
        pass



    # def add_item(self, item):
    #     """Adds item to JSON store"""
    #     from uc3m_travel import HotelManagementException
    #     try:
    #         reservation_found = super().find_item(item.localizer, "_HotelReservation__localizer")
    #         if reservation_found:
    #             raise HotelManagementException("Reservation Already Exists")
    #         for existing_item in self._data_list:
    #             if item.id_card == existing_item["_HotelReservation__id_card"]:
    #                 raise HotelManagementException("This ID card has another reservation")
    #         super().save_data(item)
    #     except HotelManagementException as ex:
    #         # Handle specific exceptions raised by find_item or add_item methods
    #         raise HotelManagementException("Error adding reservation") from ex


