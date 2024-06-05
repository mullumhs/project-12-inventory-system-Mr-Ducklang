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

    def add_item(self, item):
        #check duplicate
        for existing_item in self.items:
            if existing_item.get_name() == item.get_name():
                print("Error! Item already exists, item not added")
                return False
        self.items.append(item)
        print("Item has been added")
        return True


    def remove_item(self, name):
        for i, existing_item in enumerate(self.items):
            if existing_item.get_name() == name:
                del self.items[i]
                print("Item has been deleted")
                return True
        print("Item not found")
        return False


    def update_item_price(self, name, new_price):
        for existing_item in self.items:
            if existing_item.get_name() == name:
                existing_item.set_price(new_price)
                print(f"\nUpdated Price for {existing_item.get_name()}")
                return True
        print("Error! Item not found")
        return False
                


    def display_items(self):
        print("\nExisting Items: \n")
        for item in self.items:
            print(f"Name: {item.get_name()}, Price: {item.get_price()}, Quantity: {item.get_quantity()}")


    def find_item(self, name):
        for existing_item in self.items:
            if existing_item.get_name() == name:
                return existing_item
        print("Item not found")
        return None

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



if __name__ == "__main__":
    main()
