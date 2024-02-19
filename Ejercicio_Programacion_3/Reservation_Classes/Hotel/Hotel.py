"""CODE TO MANAGE HOTEL ENTRIES"""
# pylint: disable = invalid-name
import json


class Hotel:
    """Class representing a hotel."""

    def __init__(self, name, location, rooms):
        """Initialize a Hotel object."""
        self.name = name
        self.location = location
        self.rooms = rooms

    def to_dict(self):
        """Convert the Hotel object to a dictionary."""
        return {
            "name": self.name,
            "location": self.location,
            "rooms": self.rooms
        }

    def __str__(self):
        """String representation of the Hotel object."""
        return f"Hotel: {self.name}, Location: {self.location}," \
               f" Rooms: {self.rooms}"


class HotelController:
    """Class to manage operations related to the hotels."""

    def __init__(self, filename):
        """Initialize a HotelManager object."""
        self.filename = filename
        with open(self.filename, 'a', encoding='utf8') as file:
            file.write("")

    def create_hotel(self, hotel):
        """Create a new hotel."""
        hotels = self._read_hotels()
        if any(h['name'] == hotel.name for h in hotels):
            print("Error: Hotel with the same name already exists.")
            return
        with open(self.filename, 'a', encoding='utf8') as file:
            file.write(json.dumps(hotel.to_dict()) + '\n')

    def delete_hotel(self, hotel_name):
        """Delete a hotel."""
        hotels = self._read_hotels()
        hotels = [h for h in hotels if h['name'] != hotel_name]
        self._rewrite_hotels(hotels)

    def display_hotel_info(self, hotel_name):
        """Display information about a hotel."""
        hotels = self._read_hotels()
        for hotel in hotels:
            if hotel['name'] == hotel_name:
                return Hotel(**hotel)
        print("Error: Hotel not found.")
        return None

    def modify_hotel_info(self, hotel_name, new_info):
        """Modify information about a hotel."""
        hotels = self._read_hotels()
        found = False
        for hotel in hotels:
            if hotel['name'] == hotel_name:
                hotel.update(new_info)
                found = True
                break
        if not found:
            print("Error: Hotel not found.")
        else:
            self._rewrite_hotels(hotels)

    def _read_hotels(self):
        """Read hotels data from file."""
        try:
            with open(self.filename, 'r', encoding='utf8') as file:
                hotels = [json.loads(line) for line in file]
            return hotels
        except FileNotFoundError:
            print("Error: File not found.")
            return []

    def _rewrite_hotels(self, hotels):
        """Rewrite hotels data to file."""
        try:
            with open(self.filename, 'w', encoding='utf8') as file:
                for hotel in hotels:
                    file.write(json.dumps(hotel) + '\n')
        except FileNotFoundError:
            print("Error: File not found.")
