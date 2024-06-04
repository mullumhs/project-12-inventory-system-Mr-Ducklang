"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                                LAB 2
-----------------------------------------------------------------------------------------------
- File Name: lab2.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Extend the functionality developed in Lab 1 by creating an InventoryManager class 
               that acts as a facade for managing an inventory of items. Demonstrate the use of 
               encapsulation and the facade design pattern through practical examples.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Step 1: Import the Item class from lab1.py
from lab1 import Item


# Step 2: Define the InventoryManager class as a facade to handle the inventory operations.
# It should include methods to add, remove, update, and display items in the inventory.

class ItemManager:
    def __init__(self):
        self.items = []

    def add_item(self, Item):
        #check duplicate
        for existing_item in self.items:
            if existing_item.get_name() == Item.get_name():


    def remove_item(self, name):
        print("Item removed")


    def update_item_price(self, name, new_price):
        print("Item updated")


    def display_items(self):
        print("Displaying items")


    def find_item(self, name):
        print("Item found")

# Step 2: Create instances of the Item class and InventoryManager, then demonstrate their usage.
# E.g. add items to the inventory, remove items, update items, and display the inventory.

def main():
    manager = ItemManager()

    #Creating some items
    Car1 = Item("Miata", 12000, 1)
    Car2 = Item("Jeremy", 1000, 1)
    Food1 = Item("InstantNoodles", 5, 5)
    
    # Add items to the manager
    manager.add_item(Car1)
    manager.add_item(Car2)
    manager.add_item(Food1)
    
    # Display current items
    manager.display_items()
    
    # Update the price of items
    manager.update_item_price("Miata", 13500)
    
    # Remove items
    manager.remove_item("InstantNoodles")

   # Display current items again
    manager.display_items()



if "__name__" == "__main__":
    main()
