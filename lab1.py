"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                                LAB 1
-----------------------------------------------------------------------------------------------
- File Name: lab1.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Create a class named Item that represents a generic item in an inventory system.
               Implement encapsulation using private attributes and public getters and setters.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Step 1: Define the Item class with initialisation that uses setters for name, price, and quantity.
# Instead of directly setting private attributes in the __init__ method, use the class's own setters
# We will define the setters in later steps to add validation to the setting of these attributes.

class Item:
    def __init__(self, name, price, quantity):
        self.set_name(name)
        self.set_price(price)
        self.set_quantity(quantity)

# Step 2: Implement a getter for the name attribute.
# This method should simply return the value of the private _name attribute.        
        
    def get_name(self):
        return self._name

# Step 3: Implement a setter for the name attribute.
# This method should check if the provided value is a string before setting the _name attribute.
# If the value is not a string, it should raise a ValueError.

    def set_name(self, new_name):
        if not isinstance(new_name, str):
            raise ValueError("New name is not a string!")
        self._name = new_name

# Step 4: Implement a getter for the price attribute.
# This method should return the price formatted as a string with two decimal places.
    def get_price(self):
        return f"${self._price:.2f}"

# Step 5: Implement a setter for the price attribute.
# This method should check if the provided value is a non-negative number before setting the _price attribute.
# If the value is negative, it should raise a ValueError.
    def set_price(self, new_price):
        if new_price < 0:
            raise ValueError("New price cannot be a negative!")
        self._price = new_price

# Step 6: Implement a getter for the quantity attribute.
# This method should simply return the value of the private _quantity attribute.
    def get_quantity(self):
        return self._quantity

# Step 7: Implement a setter for the quantity attribute.
# This method should check if the provided value is a non-negative integer before setting the _quantity attribute.
# If the value is negative, it should raise a ValueError.
    def set_quantity(self, new_quantity):
        if new_quantity < 0:
            raise ValueError("New Quantity Cannot be a negative!")
        self._quantity = new_quantity

# Step 8: Create instances of the Item class and demonstrate the use of getters and setters.
# For example, create a new Item and attempt to set its attributes with both valid and invalid values.
# Print the outputs using the getters to show how the data is managed internally.

if __name__ == "__main__":
    #Valid Miata
    try:
        valid_item = Item("Miata", 12000, 1)
        print(f"Successfully created Miot :D, It is a {valid_item.get_name()} (duh), it costs {valid_item.get_price()} and there is {valid_item.get_quantity()}")
        
    except Exception as e:
        print("Error creating Miot D:", e)
        
    #Invalid Miata Price
    print()
    try:
        invalid_item_price = Item("Miata", -12.000, 1)
    except ValueError as e:
        print("Error creating Miot D:", e)

    #Invalid Miata quantity
    print()
    try:
        invalid_item_quantity = Item("Miata", 12.000, -1)
    except ValueError as e:
        print("Error creating Miot D:", e)
        
    #updating price
    print()
    try:
        valid_item.set_price(13500)
        print("Successfully updated price, Miot is more expensive :(, it now costs", valid_item.get_price())
        
    except ValueError as e:
        print("Error setting price", e)