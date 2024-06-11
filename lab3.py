"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                                LAB 3
-----------------------------------------------------------------------------------------------
- File Name: lab3.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Develop a user interface for the Inventory Management System. This interface will
               allow users to interact with the InventoryManager to add, update, remove, and view
               items in the inventory using a command-line interface.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Step 1: Import necessary classes (Item class from lab1, InventoryManager class from lab2)
from lab1 import Item
from lab2 import ItemManager


# Step 2: Define an add_item function that prompts the user for item details and adds the item to the inventory
def add_item_ui(manager):
    name = input("What item do you want to add? ")
    price = float(input(f"How much does the {name} cost? "))
    quantity = float(input("How many are there? "))
    item = Item(name, price, quantity)
    if manager.add_item(item):
        print(f"{name} has been added succesfully!")
    else:
        print(f"failed to add {name}")
    
# Step 3: Define an update_item function that prompts the user for item details and updates the item in the inventory
def update_item_ui(manager):
    name = input("What item is being updated? ")
    price = input("What is the new price? (Leave blank to keep price the same): ")
    quantity = input("What is the new quantity? (Leave blank to keep price the same):")
    if price:
         price = float(price)
    else:
         price = None
    if quantity:
         quantity = float(quantity)
    else:
         quantity = None
    if manager.update_item_price(name, price):
         print("Successfully updated")
    else:
         print("No changes made, either input was blank or item not found")
# Step 4: Define a remove_item function that prompts the user for an item name and removes the item from the inventory
def remove_item_ui(manager):
    name = input("What item is being removed? ")
    if manager.remove_item(name):
         print(f"{name} removed successfully!")
    else:
         print("Error, item not found!")
 
# Step 5: Define a display_inventory function that displays all items in the inventory
def display_items_ui(manager):
    manager.display_items()
    choice = input("Enter any Key to return to menu")

def main():
    # Step 6: Initialise an instance of InventoryManager
    manager = ItemManager()

    # Step 7: Use the actions dictionary to map user input to the corresponding functions
    actions = {
            '1': add_item_ui,
            '2': update_item_ui,
            '3': remove_item_ui,
            '4': display_items_ui,
     }
    
    while True:
        print("\nInventory Management System")
        print("1. Add Item")
        print("2. Update Item")
        print("3. Remove Item")
        print("4. Display Inventory")
        print("5. Exit\n")
        choice = input("Enter choice: ")
        print()

        # Step 8: Implement the logic to call the appropriate function based on user input
        # Exit the loop if the user chooses 5, otherwise display an error message for invalid choices
        if choice == '5':
                print("Goodbye!")
                break
        elif choice in actions:
                actions[choice](manager)
        else:
            print("Error, Invalid Choice, please select an option between 1-5.")
        

if __name__ == "__main__":
    main()