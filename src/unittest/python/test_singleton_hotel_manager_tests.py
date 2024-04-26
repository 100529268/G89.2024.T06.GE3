"""Module for testing singleton-hotel manager"""
import unittest
from uc3m_travel import HotelManager
from uc3m_travel.storage import JsonStore


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

        # request_json_store_1 = JsonStore('test_singleton.json')
        # request_json_store_2 = JsonStore('test_singleton.json')
        # request_json_store_3 = JsonStore('test_singleton.json')
        #
        # self.assertEqual(request_json_store_1, request_json_store_2)
        # self.assertEqual(request_json_store_2, request_json_store_3)
        # self.assertEqual(request_json_store_3, request_json_store_1)



