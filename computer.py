class Computer:
    # What attributes will it need?
    #Price, OS, Year Made, Manufacturer
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, 
                info:str, 
                processor: str,
                hard_drive: int,
                memory: int,
                os: str,
                year: int,
                price: int):
        
        self.description = info
        self.processor_type = processor
        self.hard_drive_capacity = hard_drive
        self.memory = memory
        self.operating_system = os
        self.year = year
        self.price = price

    def update_price(self, new_price: int):
        self.price = new_price
    
    def update_os(self, new_os: str):
        self.operating_system = new_os



    # What methods will you need?