"""Hotel reservation class"""
import hashlib
from datetime import datetime

from uc3m_travel.attributes import CreditCard, IDCard, ArrivalDate, NameSurname, PhoneNumber, RoomType, NumDays


class HotelReservation:
    """Class for representing hotel reservations"""
    #pylint: disable=too-many-arguments, too-many-instance-attributes
    def __init__(self,
                 id_card: str,
                 credit_card_number: str,
                 name_surname: str,
                 phone_number: str,
                 room_type: str,
                 arrival: str,
                 num_days: int):
        """constructor of reservation objects"""
        self.__credit_card_number = CreditCard(credit_card_number).value
        self.__id_card = IDCard(id_card).value
        justnow = datetime.utcnow()
        self.__arrival = ArrivalDate(arrival).value
        self.__reservation_date = datetime.timestamp(justnow)
        self.__name_surname = NameSurname(name_surname).value
        self.__phone_number = PhoneNumber(phone_number).value
        self.__room_type = RoomType(room_type).value
        self.__num_days = NumDays(num_days).value
        self.__localizer = hashlib.md5(str(self).encode()).hexdigest()

    def __str__(self):
        """return a json string with the elements required to calculate the localizer"""
        #VERY IMPORTANT: JSON KEYS CANNOT BE RENAMED
        json_info = {"id_card": self.__id_card,
                     "name_surname": self.__name_surname,
                     "credit_card": self.__credit_card_number,
                     "phone_number:": self.__phone_number,
                     "reservation_date": self.__reservation_date,
                     "arrival_date": self.__arrival,
                     "num_days": self.__num_days,
                     "room_type": self.__room_type,
                     }
        return "HotelReservation:" + json_info.__str__()

    @property
    def credit_card(self):
        """property for getting and setting the credit_card number"""
        return self.__credit_card_number

    @credit_card.setter
    def credit_card(self, value):
        self.__credit_card_number = value

    @property
    def id_card(self):
        """property for getting and setting the id_card"""
        return self.__id_card

    @id_card.setter
    def id_card(self, value):
        self.__id_card = value

    @property
    def localizer(self):
        """Returns the md5 signature"""
        return self.__localizer

    @property
    def room_type(self):
        """property for getting and setting the room_type"""
        return self.__room_type

    @property
    def num_days(self):
        """property for getting and setting the num_days"""
        return self.__num_days

    @property
    def phone_number(self):
        """property for getting and setting the phone_number"""
        return self.__phone_number

    @property
    def arrival(self):
        """property for getting and setting the arrival_date"""
        return self.__arrival

    @property
    def name_surname(self):
        """property for getting and setting the name_surname"""
        return self.__name_surname