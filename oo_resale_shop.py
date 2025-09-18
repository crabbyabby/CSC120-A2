"""
    Filename: oo_resale_shop.py
Description: an example of object-oriented code to a computer shop,
             part of A2: Object-ification, CSC120: Object-Oriented Programming
             as taught at Smith College in Fall 2025. Based on an example by Sami Islam.
     Author: Abigail Lei
       Date: 17 September 2025
"""

#NEED TO CHNAGE CODE TO TAKE IN ITEM ID IN THE NEW WAY WE ARE DOING IT

#importing necessary modules for the code
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
        if self.balance < price:
            print("The store cannot afford to buy this computer.")
        else:
            self.inventory.append(computer)
            self.balance -= price
            return len(self.inventory) - 1
    
    """
    Takes in an int of the Computer's ID and removes it from the inventory, and adds the 
    price of the computer to the store's balance
    """  
    def sell(self, item_id: int):
        index = -1
        for i in range(len(self.inventory)):
            if self.inventory[i].get_id() == item_id:
                index = i
        if self.inventory[i] is not None:
            self.balance += self.inventory[i].get_price()
            self.inventory.pop(i)
            print("Item", item_id, "sold!")
        else: 
            print("Item", item_id, "not found. Please select another item to sell.")

    """
    Takes in an int of the Computer's ID and an optional string of the new operating system
    and refurbishes it, setting a new price and potentially replacing the operating system.
    """  
    def refurbish(self, item_id: int, new_os: Optional[str] = None):
        index = -1
        for i in range(len(self.inventory)):
            if self.inventory[i].get_id() == item_id:
                index = i
        if self.inventory[i] is not None:
            computer = self.inventory[i] # locate the computer
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
        
    """
    Prints all the items in the inventory and a description of them (if it isn't empty), prints error otherwise
    """  
    def print_inv(self):
        statement = ""
        if self.inventory:
            for item in self.inventory:
                statement += (f"\nItem ID: {item.id} : {item.description}, {item.year}, ${item.price}")
            return statement
        else:
            return "The inventory is empty. There is nothing to display."

    """
    Returns the balance of the store
    """    
    def get_balance(self):
        return self.balance

#Testing the code
def main():
    comp1 = Computer("2019 MacBook Pro", "Intel", 256, 16, "High Sierra", 2019, 1000, 111)
    comp2 = Computer("2020 Windows", "Intel", 512, 64, "Linux", 2022, 1100, 11)
    store = ResaleShop(10000)
    store.buy(comp1, 1000)
    store.buy(comp2, 2000)

    print(store.print_inv())
    store.sell(111)
    print(store.print_inv())
    print(store.get_balance())


main()
