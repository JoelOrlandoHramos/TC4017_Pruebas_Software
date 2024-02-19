"""CODE TO TEST METHOD AND CLASSES
FOR HOTEL.PY"""
# pylint: disable = invalid-name

import unittest
from Hotel import Hotel, HotelController


class TestHotelController(unittest.TestCase):
    """Class to manage the unit test cases"""

    def setUp(self):
        """Initializing a file where our tests results
        be saved"""
        self.filename = "test_hotels.json"
        self.hotel_controller = HotelController(self.filename)

    def test_create_hotel(self):
        """TEST CASE 1. Successfully create Hotel Class"""
        hotel_entry = Hotel("Hotel Grand Plaza", "New York", 100)
        self.hotel_controller.create_hotel(hotel_entry)
        new_hotel = self.hotel_controller.display_hotel_info(
            "Hotel Grand Plaza")
        self.assertEqual(new_hotel.name, "Hotel Grand Plaza")
        if new_hotel.name == "Hotel Grand Plaza":
            print("TEST CASE 1\n\n")
            print(f'New Hotel entry\n'
                  f'{new_hotel}')
            print('-' * 50)

    def test_delete_hotel(self):
        """TEST CASE 2. Deleting a hotel entry"""
        new_hotel = Hotel("Hotel Hollywood", "Los Angeles", 50)
        self.hotel_controller.create_hotel(new_hotel)

        # We print the created hotel from JSON FILE
        print("TEST CASE 2\n\n")
        print("First we added a new hotel entry:\n")
        print(self.hotel_controller.display_hotel_info("Hotel Hollywood"))

        print("After making sure it is in our JSON File. "
              "We delete it and get the following error\n\n")

        self.hotel_controller.delete_hotel("Hotel Hollywood")
        deleted_hotel = self.hotel_controller.display_hotel_info(
            "Hotel Hollywood")
        self.assertIsNone(deleted_hotel)
        print('-' * 50)

    def test_create_and_modify_hotel(self):
        """Test creating a new hotel entry and then modifying it"""

        new_hotel = Hotel("Hotel Soberano", "Chihuahua", 200)
        self.hotel_controller.create_hotel(new_hotel)
        retrieved_hotel = self.hotel_controller.display_hotel_info(
            "Hotel Soberano")
        self.assertEqual(retrieved_hotel.name, "Hotel Soberano")

        # We print the created hotel from JSON FILE
        print("TEST CASE 3\n\n")
        print("First we added a new hotel entry:\n")
        print(self.hotel_controller.display_hotel_info("Hotel Soberano"))

        # Modify the hotel information
        new_info = {"location": "Los Angeles", "rooms": 150}
        self.hotel_controller.modify_hotel_info("Hotel Soberano", new_info)
        modified_hotel = self.hotel_controller.display_hotel_info(
            "Hotel Soberano")
        self.assertEqual(modified_hotel.location, "Los Angeles")
        self.assertEqual(modified_hotel.rooms, 150)

        print("After making sure it is in our JSON File. "
              "We modfy it and get the following info:\n\n")
        print(self.hotel_controller.display_hotel_info("Hotel Soberano"))
        print('-' * 50)

    def test_get_nonexistent_hotel(self):
        """Test getting information for a hotel that does not exist"""
        print("TEST CASE 4\n\n")
        nonexistent_hotel = self.hotel_controller.display_hotel_info(
            "Whichever Hotel")
        self.assertIsNone(nonexistent_hotel)
        print('-' * 50)

    def test_create_existing_hotel(self):
        """Test creating a hotel entry with the same name as an existing one"""
        print("TEST CASE 5\n\n")
        new_hotel = Hotel("Hotel Soberano", "Las Angeles", 200)
        self.hotel_controller.create_hotel(new_hotel)
        print('-' * 50)


if __name__ == '__main__':
    unittest.main()
