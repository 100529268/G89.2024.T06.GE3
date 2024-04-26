"""Module for testing singleton-hotel manager"""
import unittest
from uc3m_travel import HotelManager
from uc3m_travel.storage import JsonStore
from uc3m_travel.storage import ReservationJsonStore
from uc3m_travel.storage import StayJsonStore
from uc3m_travel.storage import CheckoutJsonStore


class TestingSingleton(unittest.TestCase):
    """Test case for the singletons"""
    def test_singleton_access_manager(self):
        """Instance the three singletons and test they're equal
        Instance objects from non singleton class and test they're different"""


        hotel_manager_1 = HotelManager()
        hotel_manager_2 = HotelManager()
        hotel_manager_3 = HotelManager()

        self.assertEqual(hotel_manager_1, hotel_manager_2)
        self.assertEqual(hotel_manager_2, hotel_manager_3)
        self.assertEqual(hotel_manager_3, hotel_manager_1)

        reservation_json_store_1 = ReservationJsonStore()
        reservation_json_store_2 = ReservationJsonStore()
        reservation_json_store_3 = ReservationJsonStore()

        self.assertEqual(reservation_json_store_1, reservation_json_store_2)
        self.assertEqual(reservation_json_store_2, reservation_json_store_3)
        self.assertEqual(reservation_json_store_3, reservation_json_store_1)
        
        stay_json_store_1 = StayJsonStore()
        stay_json_store_2 = StayJsonStore()
        stay_json_store_3 = StayJsonStore()

        self.assertEqual(stay_json_store_1, stay_json_store_2)
        self.assertEqual(stay_json_store_2, stay_json_store_3)
        self.assertEqual(stay_json_store_3, stay_json_store_1)
        
        checkout_json_store_1 = CheckoutJsonStore()
        checkout_json_store_2 = CheckoutJsonStore()
        checkout_json_store_3 = CheckoutJsonStore()

        self.assertEqual(checkout_json_store_1, checkout_json_store_2)
        self.assertEqual(checkout_json_store_2, checkout_json_store_3)
        self.assertEqual(checkout_json_store_3, checkout_json_store_1)




