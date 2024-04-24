"""Module for the hotel manager"""
import json
from uc3m_travel.hotel_management_exception import HotelManagementException
from uc3m_travel.hotel_reservation import HotelReservation
from uc3m_travel.hotel_stay import HotelStay
from uc3m_travel.attributes import CreditCard, IDCard, Localizer, RoomKey
from uc3m_travel.storage.reservation_json_store import ReservationJsonStore
from uc3m_travel.storage.stay_json_store import StayJsonStore

from uc3m_travel.storage import CheckoutJsonStore


class HotelManager:
    """Class with all the methods for managing reservations and stays"""

    def __init__(self):
        pass

    def room_reservation(self,
                         credit_card: str,
                         name_surname: str,
                         id_card: str,
                         phone_number: str,
                         room_type: str,
                         arrival_date: str,
                         num_days: int) -> str:
        """manges the hotel reservation: creates a reservation and saves it into a json file"""
        my_reservation = HotelReservation(id_card=id_card,
                                          name_surname=name_surname,
                                          phone_number=phone_number,
                                          room_type=room_type,
                                          arrival=arrival_date,
                                          num_days=num_days,
                                          credit_card_number=credit_card)
        ReservationJsonStore().add_reservation(my_reservation)
        return my_reservation.localizer

    def guest_arrival(self, file_input: str) -> str:
        my_id_card, my_localizer = self.read_input_from_file(file_input)
        my_checkin = HotelStay(my_localizer, my_id_card)
        StayJsonStore().add_stay(my_checkin)
        return my_checkin.room_key

    def read_input_from_file(self, file_input):
        """manages the arrival of a guest with a reservation"""
        try:
            with open(file_input, "r", encoding="utf-8", newline="") as file:
                input_list = json.load(file)
        except FileNotFoundError as ex:
            raise HotelManagementException("Error: file input not found") from ex
        except json.JSONDecodeError as ex:
            raise HotelManagementException("JSON Decode Error - Wrong JSON Format") from ex

        try:
            my_localizer = input_list["Localizer"]
            my_id_card = input_list["IdCard"]
        except KeyError as e:
            raise HotelManagementException("Error - Invalid Key in JSON") from e

        # Validate IdCard and Localizer
        IDCard(my_id_card)
        Localizer(my_localizer)

        return my_id_card, my_localizer

    def guest_checkout(self, room_key: str) -> bool:
        """manages the checkout of a guest"""
        HotelStay.get_stay_from_room_key(room_key)
        CheckoutJsonStore().add_stay(room_key)
        return True
