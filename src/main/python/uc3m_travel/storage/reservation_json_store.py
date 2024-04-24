"""Module for the hotel manager"""

from uc3m_travel.hotel_management_exception import HotelManagementException
from uc3m_travel.hotel_management_config import JSON_FILES_PATH
from uc3m_travel.storage.json_store import JsonStore


class ReservationJsonStore(JsonStore):
    _file_name = JSON_FILES_PATH + "store_reservation.json"

    def __init__(self):
        super().__init__(self._file_name)

    def find_reservation(self, localizer, msg):
        return super().find_item("_HotelReservation__localizer", localizer, msg)

    def add_reservation(self, reservation):
        msg = "pass error"
        # checks for duplicate reservations
        if super().find_item("_HotelReservation__localizer", reservation.localizer, msg):
            raise HotelManagementException("Reservation already exists")

        if super().find_item("_HotelReservation__id_card", reservation.id_card, msg):
            raise HotelManagementException("This ID card has another reservation")

        super().add_item(reservation)
