"""
    Filename: oo_resale_shop.py
Description: an example of object-oriented code to a computer shop,
             part of A2: Object-ification, CSC120: Object-Oriented Programming
             as taught at Smith College in Fall 2025. Based on an example by Sami Islam.
     Author: Abigail Lei
       Date: 17 September 2025
"""

from typing import Optional
from computer import Computer

class ResaleShop:

    # What attributes will it need?
    inventory: list
    balance: float

    #Inventory, store balance, buying, selling, refurbishing
    """
    Takes in a float containing the starting balance of the computer shop
    and creates an inventory for the shop.
    """
    def __init__(self, balance: float):
        self.inventory = []
        self.balance = balance

    """
    Takes in an object of the computer class and an int as the price and 
    adds the purchased computer to the resale shop's inventory, and subtracts
    the price of the computer from the store's balance
    """
    def buy(self, computer: "Computer", price: int):
        self.inventory.append(computer)
        self.balance -= price
        return len(self.inventory) - 1
    
    """
    Takes in an int of the Computer's ID and removes it from the inventory, and adds the 
    price of the computer to the store's balance
    """  
    def sell(self, item_id: int):
        if self.inventory[item_id] is not None:
            self.balance += self.inventory[item_id].get_price()
            self.inventory.pop(item_id)
            print("Item", item_id, "sold!")
        else: 
            print("Item", item_id, "not found. Please select another item to sell.")

    def refurbish(self, item_id: int, new_os: Optional[str] = None):
        if self.inventory[item_id] is not None:
            computer = self.inventory[item_id] # locate the computer
            if int(computer.get_year()) < 2000:
                computer.update_price(0) # too old to sell, donation only
            elif int(computer.get_year()) < 2012:
                computer.update_price(250) # heavily-discounted price on machines 10+ years old
            elif int(computer.get_year()) < 2018:
                computer.update_price(550) # discounted price on machines 4-to-10 year old machines
            else:
                computer.update_price(1000) # recent stuff

            if new_os is not None:
                computer.update_os(new_os) # update details after installing new OS
        else:
            print("Item", item_id, " is not found. Please select another item to refurbish.")
        

    def print_inv(self):
        if self.inventory:
            for index, item in enumerate(self.inventory):
                print(f"Item ID: {index} : {item.description}, {item.year}, ${item.price}")
        else:
            print("The inventory is empty. There is nothing to display.")


    # What methods will you need?