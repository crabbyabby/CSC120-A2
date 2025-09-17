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
        self.inventory.append(Computer)
        return len(self.inventory) - 1
    
    def sell(self, item_id: int):
        if self.inventory[item_id] is not None:
            self.inventory.pop(item_id)
            print("Item", item_id, "sold!")
        else: 
            print("Item", item_id, "not found. Please select another item to sell.")

    def refurbish(item_id: int, new_os: Optional[str] = None):
        if self.inventory[item_id] is not None:
            computer = self.inventory[item_id] # locate the computer
            if int(computer["year_made"]) < 2000:
                computer["price"] = 0 # too old to sell, donation only
            elif int(computer["year_made"]) < 2012:
                computer["price"] = 250 # heavily-discounted price on machines 10+ years old
            elif int(computer["year_made"]) < 2018:
                computer["price"] = 550 # discounted price on machines 4-to-10 year old machines
            else:
                computer["price"] = 1000 # recent stuff

            if new_os is not None:
                computer["operating_system"] = new_os # update details after installing new OS
        else:
            print("Item", item_id, "not found. Please select another item to refurbish.")
        

    def print_inv(self):
        if self.inventory:
            for item in self.inventory:
                print(f'Item ID: {self.inventory.index(item)} : {item}')
        else:
            print("The inventory is empty. There is nothing to display.")


    # What methods will you need?