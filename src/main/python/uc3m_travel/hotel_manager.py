"""Module for the hotel manager"""
from uc3m_travel.hotel_reservation import HotelReservation
from uc3m_travel.hotel_stay import HotelStay
from uc3m_travel.storage.reservation_json_store import ReservationJsonStore
from uc3m_travel.storage.stay_json_store import StayJsonStore

from uc3m_travel.storage import CheckoutJsonStore
from uc3m_travel.utils.json_parser import JsonParser


class HotelManager:
    class __HotelManager:
        """Class with all the methods for managing reservations and stays"""

        # pylint: disable=too-many-arguments, too-many-instance-attributes
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
            """Takes care of guest arrivals"""
            my_parser = JsonParser(file_input)
            my_id_card, my_localizer = my_parser.read_input_from_file()
            my_checkin = HotelStay(my_localizer, my_id_card)
            StayJsonStore().add_stay(my_checkin)
            return my_checkin.room_key


        def guest_checkout(self, room_key: str) -> bool:
            """manages the checkout of a guest"""
            HotelStay.get_stay_from_room_key(room_key)
            CheckoutJsonStore().add_stay(room_key)
            return True

    __instance = None

    def __new__(cls):
        if not HotelManager.__instance:
            HotelManager.__instance = HotelManager.__HotelManager()
        return HotelManager.__instance