"""CODE TO MANAGE CUSTOMER ENTRIES"""
# pylint: disable = invalid-name
import json


class Customer:
    """Class representing a customer."""

    def __init__(self, name, lastname, email):
        """Initialize a Customer object."""
        # Check if name, lastname, and email are provided
        if not name or not lastname or not email:
            print(ValueError("Error: Name, lastname, and email are required."))
        self.name = name
        self.lastname = lastname
        self.email = email

    def to_dict(self):
        """Convert the Customer object to a dictionary."""
        return {
            "name": self.name,
            "lastname": self.lastname,
            "email": self.email
        }

    def __str__(self):
        """String representation of the Customer object."""
        return f"Customer Name: {self.name}, Last Name: " \
               f"{self.lastname}, Email: {self.email}"


class CustomerManager:
    """Class to manage operations related to customers."""

    def __init__(self, filename):
        """Initialize a CustomerManager object."""
        self.filename = filename

    def create_customer(self, customer):
        """Create a new customer."""
        with open(self.filename, 'a', encoding='utf8') as file:
            file.write(json.dumps(customer.to_dict()) + '\n')

    def delete_customer(self, customer_email):
        """Delete a customer."""
        customers = self._read_customers()
        if not any(c['email'] == customer_email for c in customers):
            print(ValueError("Error: Customer not found."))
        customers = [c for c in customers if c['email'] != customer_email]
        self._rewrite_customers(customers)

    def display_customer_info(self, customer_email):
        """Display information about a customer."""
        customers = self._read_customers()
        for customer in customers:
            if customer['email'] == customer_email:
                return Customer(**customer)
        print("Error: Customer not found.")
        return None

    def modify_customer_info(self, customer_email, new_info):
        """Modify information about a customer."""
        customers = self._read_customers()
        found = False
        for customer in customers:
            if customer['email'] == customer_email:
                customer.update(new_info)
                found = True
                break
        if not found:
            print("Error: Customer not found.")
        else:
            self._rewrite_customers(customers)

    def _read_customers(self):
        """Read customers data from file."""
        try:
            with open(self.filename, 'r', encoding='utf8') as file:
                customers = [json.loads(line) for line in file]
            return customers
        except FileNotFoundError:
            print("Error: File not found.")
            return []

    def _rewrite_customers(self, customers):
        """Rewrite customers data to file."""
        try:
            with open(self.filename, 'w', encoding='utf8') as file:
                for customer in customers:
                    file.write(json.dumps(customer) + '\n')
        except FileNotFoundError:
            print("Error: File not found.")
