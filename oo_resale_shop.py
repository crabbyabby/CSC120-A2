from typing import Optional

class ResaleShop:

    # What attributes will it need?
    inventory: list
    balance: float

    #Inventory, store balance, buying, selling, refurbishing
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, balance: float):
        self.inventory = []
        self.balance = balance

    def buy(self):
        self.inventory.append(Computer)
        return len(self.inventory) - 1
    
    def sell(self, item_id: int):
        if self.inventory[item_id] is not None:
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