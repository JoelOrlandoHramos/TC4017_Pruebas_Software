"""CODE TO Evaluate Customers.py"""
# pylint: disable = invalid-name
import unittest
from Customers import Customer, CustomerManager


class TestCustomerManager(unittest.TestCase):
    """Class to manage the unit test cases"""
    def setUp(self):
        """Initialize a file to store data """
        self.filename = "test_customers.json"
        self.customer_manager = CustomerManager(self.filename)

    def test_create_and_display_customer_info(self):
        """Test creating a customer and then
         displaying their information"""
        new_customer = Customer(name="Joel", lastname="Hernandez",
                                email="joel@example.com")
        self.customer_manager.create_customer(new_customer)
        retrieved_customer = self.customer_manager.display_customer_info(
            "joel@example.com")
        self.assertEqual(retrieved_customer.name, "Joel")
        self.assertEqual(retrieved_customer.lastname, "Hernandez")
        self.assertEqual(retrieved_customer.email, "joel@example.com")
        if retrieved_customer.name == "Joel" \
                and retrieved_customer.lastname == "Hernandez" \
                and retrieved_customer.email == "joel@example.com":
            print("TEST CASE 1\n\n")
            print(f'New Customer entry\n'
                  f'{retrieved_customer}')
            print('-' * 50)

    def test_modify_customer_info(self):
        """Test creating a customer, modifying their information,
        and then displaying the modified information"""
        new_customer = Customer(name="Taemin", lastname="Lee",
                                email="leet@example.com")
        self.customer_manager.create_customer(new_customer)

        # We print the created Customer from JSON FILE
        print("TEST CASE 2\n\n")
        print("First we added a new Customer entry:\n")
        print(self.customer_manager.display_customer_info(
            customer_email="leet@example.com"))

        # We modify name and lastname but keep the email
        modified_info = {"name": "Jane", "lastname": "Smith"}
        self.customer_manager.modify_customer_info("leet@example.com",
                                                   modified_info)

        modified_customer = self.customer_manager.display_customer_info(
            "leet@example.com")
        self.assertEqual(modified_customer.name, "Jane")
        self.assertEqual(modified_customer.lastname, "Smith")
        self.assertEqual(modified_customer.email, "leet@example.com")

        print("\nAfter making sure it is in our JSON File. "
              "We modfy it and get the following info:\n\n")
        print(self.customer_manager.display_customer_info(
            "leet@example.com"))
        print('-' * 50)

    def test_create_customer_missing_info(self):
        """Test creating a customer with missing information"""
        print("TEST CASE 3\n\n")
        print("No complete information is given so "
              "program should print an error\n\n")
        self.customer_manager.create_customer(Customer("", "Doe",
                                                       "john@example.com"))
        print('-' * 50)

    def test_delete_nonexistent_customer(self):
        """Test deleting a nonexistent customer"""
        print("TEST CASE 4\n\n")
        print("There is no such customer to delete so"
              "program should print an error\n\n")
        non_existent_email = "nonexistent@example.com"
        self.customer_manager.delete_customer(non_existent_email)
        print('-' * 50)


if __name__ == "__main__":
    unittest.main()
