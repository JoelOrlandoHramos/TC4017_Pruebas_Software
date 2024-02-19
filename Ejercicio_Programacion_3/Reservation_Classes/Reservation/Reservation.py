"""CODE TO MANAGE RESERVATIONS"""
# pylint: disable = invalid-name
import json


class Reservation:
    """Class representing a reservation."""

    def __init__(self, customer, hotel, room_number, start_date, end_date):
        # pylint: disable = too-many-arguments
        """Initialize a Reservation object."""
        if not customer or not hotel or not room_number \
                or not start_date or not end_date:
            print(ValueError("Error: Complete reservation "
                             "information required."))
        self.customer = customer
        self.hotel = hotel
        self.room_number = room_number
        self.start_date = start_date
        self.end_date = end_date

    def to_dict(self):
        """Convert the Reservation object to a dictionary."""
        return {
            "customer": self.customer,
            "hotel": self.hotel,
            "room_number": self.room_number,
            "start_date": self.start_date,
            "end_date": self.end_date
        }

    def __str__(self):
        """String representation of the Reservation object."""
        return f"Reservation: Customer: {self.customer}, " \
               f"Hotel: {self.hotel}, Room Number: {self.room_number}, " \
               f"Start Date: {self.start_date}, End Date: {self.end_date}"


class ReservationManager:
    """Class to manage operations related to reservations."""

    def __init__(self, filename):
        """Initialize a ReservationManager object."""
        self.filename = filename

    def create_reservation(self, reservation):
        """Create a new reservation."""
        if not self._is_room_available(reservation.hotel,
                                       reservation.room_number,
                                       reservation.start_date,
                                       reservation.end_date):
            print(ValueError("Error: Room not available for the given dates."))
        with open(self.filename, 'a', encoding='utf8') as file:
            file.write(json.dumps(reservation.to_dict()) + '\n')

    def display_reservation(self, customer_name):
        """Display information about a customer."""
        reservations = self._read_reservations()
        for reservation in reservations:
            if reservation['customer'] == customer_name:
                return Reservation(**reservation)
        print("Error: Customer not found.")
        return None

    def _is_room_available(self, hotel_name, room_number,
                           start_date, end_date):
        """Check if a room is available for the given dates."""
        reservations = self._read_reservations()
        for reservation in reservations:
            if (reservation['hotel'] == hotel_name and
                    reservation['room_number'] == room_number and
                    not (end_date <= reservation['start_date']
                         or start_date >= reservation['end_date'])):
                return False
        return True

    def cancel_reservation(self, customer_email, hotel_name):
        """Cancel a reservation."""
        reservations = self._read_reservations()
        updated_reservations = []
        for reservation in reservations:
            if reservation['customer'] != customer_email \
                    or reservation['hotel'] != hotel_name:
                updated_reservations.append(reservation)
        self._rewrite_reservations(updated_reservations)

    def _read_reservations(self):
        """Read reservations data from file."""
        try:
            with open(self.filename, 'r', encoding='utf8') as file:
                reservations = [json.loads(line) for line in file]
            return reservations
        except FileNotFoundError:
            return []

    def _rewrite_reservations(self, reservations):
        """Rewrite reservations data to file."""
        try:
            with open(self.filename, 'w', encoding='utf8') as file:
                for reservation in reservations:
                    file.write(json.dumps(reservation) + '\n')
        except FileNotFoundError:
            print("Error: File not found.")
