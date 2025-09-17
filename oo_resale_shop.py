class ResaleShop:

    # What attributes will it need?
    inventory: list
    balance: float

    #Inventory, store balance, buying, selling, refurbishing
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, balance: float):
        self.inventory = []
        self.balance = 0

    def buy(self):
        print("hi")

    def print_inv(self):
        if self.inventory:
            for item in self.inventory:
                print(f'Item ID: {self.inventory.index(item)} : {item}')
        else:
            print("The inventory is empty. There is nothing to display.")


    # What methods will you need?