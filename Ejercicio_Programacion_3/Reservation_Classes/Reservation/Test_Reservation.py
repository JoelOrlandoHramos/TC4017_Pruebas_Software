"""CODE TO TEST RESERVATION.PY"""
# pylint: disable = invalid-name
# pylint: disable = protected-access
# pylint: disable = import-error
import unittest
from Reservation import Reservation, ReservationManager


class TestReservationManager(unittest.TestCase):
    """CLASS TO MANAGE THE TEST CASES"""

    def setUp(self):
        """Initialize a file to store the reservations"""
        self.filename = "test_reservations.json"
        self.reservation_manager = ReservationManager(self.filename)

    def test_create_reservation(self):
        """Test creating a reservation and then checking its availability"""
        new_reservation = Reservation("Joel Hernandez", "Hotel Sheraton",
                                      101, "2024-02-20", "2024-02-22")
        self.reservation_manager.create_reservation(new_reservation)
        saved_reservation = self.reservation_manager.display_reservation(
            "Joel Hernandez")
        is_available = self.reservation_manager._is_room_available(
            "Hotel Sheraton",
            101, "2024-02-20", "2024-02-22")
        self.assertFalse(is_available)
        if not is_available:
            print("TEST CASE 1\n\n")
            print(f'New Reservation entry\n'
                  f'{saved_reservation}')
            print('-' * 50)

    def test_cancel_reservation(self):
        """Test creating a reservation, cancelling it,
        and then checking its availability"""

        new_reservation = Reservation("Carlos Pazos", "Hotel Marriot",
                                      98, "2024-03-20", "2024-04-22")
        self.reservation_manager.create_reservation(new_reservation)

        # We print the created Reservation from JSON FILE
        print("TEST CASE 2\n\n")
        print("First we added a new Reservation entry:\n")
        print(self.reservation_manager.display_reservation(
            "Carlos Pazos"))

        # We then cancel the reservation
        self.reservation_manager.cancel_reservation("Carlos Pazos",
                                                    "Hotel Marriot")

        # We then check availability
        is_available = self.reservation_manager._is_room_available(
            "Hotel Marriot",
            98, "2024-03-20", "2024-04-22")
        self.assertTrue(is_available)
        if is_available:
            print("\n\nSince we just had a cancellation"
                  " dates are available\n\n")
            print('-' * 50)

    def test_create_reservation_missing_info(self):
        """Test creating a reservation with missing information"""
        print("TEST CASE 3\n\n")
        print("No complete information is given so "
              "program should print an error\n\n")
        self.reservation_manager.create_reservation(Reservation(
            "", "Hotel ABC", 101,
            "2024-02-20", "2024-02-22"))
        print('-' * 50)

    def test_create_reservation_duplicate_room_number(self):
        """Test creating a reservation with a room number
         that is already reserved"""
        new_reservation1 = Reservation("Andrea Acevedo",
                                       "Hotel Yushima",
                                       101, "2024-02-20", "2024-02-22")
        new_reservation2 = Reservation("Antonio Hernandez",
                                       "Hotel Yushima",
                                       101, "2024-02-20", "2024-02-25")
        print("TEST CASE 4\n\n")
        print("Same room number has been requested by two reservations "
              "program should print an error\n\n")
        self.reservation_manager.create_reservation(new_reservation1)
        self.reservation_manager.create_reservation(new_reservation2)
        print('-' * 50)


if __name__ == "__main__":
    unittest.main()
