"""Class HotelStay (GE2.2)"""
# pylint: disable=no-member, syntax-error, no-name-in-module
from datetime import datetime
import hashlib

from uc3m_travel.hotel_reservation import HotelReservation
from uc3m_travel.hotel_management_exception import HotelManagementException
from uc3m_travel.storage.stay_json_store import StayJsonStore
from uc3m_travel.attributes import RoomKey

class HotelStay:
    """Class for representing hotel stays"""

    def __init__(self, localizer: str, id_card: str):
        """constructor for HotelStay objects"""
        self.__alg = "SHA-256"
        self.__localizer = localizer
        self.__idcard = id_card

        reservation = HotelReservation.load_reservation_from_localizer(self.localizer)
        if reservation.id_card != self.__idcard:
            raise HotelManagementException("Error: Localizer is not correct for this IdCard")

        self.__type = reservation.room_type
        justnow = datetime.utcnow()
        self.__arrival = datetime.timestamp(justnow)

        reservation_format = "%d/%m/%Y"
        date_obj = datetime.strptime(reservation.arrival, reservation_format)
        if date_obj.date() != datetime.date(datetime.utcnow()):
            raise HotelManagementException("Error: today is not reservation date")

        self.__departure = self.__arrival + (reservation.num_days * 24 * 60 * 60)
        self.__room_key = hashlib.sha256(self.__signature_string().encode()).hexdigest()

    def __signature_string(self):
        """Composes the string to be used for generating the key for the room"""
        return "{alg:" + self.__alg + ",typ:" + self.__type + ",localizer:" + \
            self.__localizer + ",arrival:" + str(self.__arrival) + \
            ",departure:" + str(self.__departure) + "}"

    @classmethod
    def get_stay_from_room_key(cls, room_key):
        """gets storred stay based on room_key"""
        stay_stores = StayJsonStore()
        stay = stay_stores.find_stay(RoomKey(room_key).value)

        if not stay:
            raise HotelManagementException("Error: room key not found")
        departure_date_timestamp = stay["_HotelStay__departure"]

        today = datetime.utcnow().date()
        if datetime.fromtimestamp(departure_date_timestamp).date() != today:
            raise HotelManagementException("Error: today is not the departure day")

        return HotelStay

    @property
    def id_card(self):
        """Property that represents the product_id of the patient"""
        return self.__idcard

    @id_card.setter
    def id_card(self, value):
        self.__idcard = value

    @property
    def localizer(self):
        """Property that represents the order_id"""
        return self.__localizer

    @localizer.setter
    def localizer(self, value):
        self.__localizer = value

    @property
    def arrival(self):
        """Property that represents the phone number of the client"""
        return self.__arrival

    @property
    def room_key(self):
        """Returns the sha256 signature of the date"""
        return self.__room_key

    @property
    def departure(self):
        """Returns the issued at value"""
        return self.__departure

    @departure.setter
    def departure(self, value):
        """returns the value of the departure date"""
        self.__departure = value
