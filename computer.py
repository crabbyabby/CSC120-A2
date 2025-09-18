"""
    Filename: computer.py
Description: an example of object-oriented code to create computers for a computer shop,
             part of A2: Object-ification, CSC120: Object-Oriented Programming
             as taught at Smith College in Fall 2025. Based on an example by Sami Islam.
     Author: Abigail Lei
       Date: 17 September 2025
"""

class Computer:

    unique_computers = set()
    
    # What attributes will it need?
    #Price, OS, Year Made
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int
    id: int
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, 
                info:str, 
                processor: str,
                hard_drive: int,
                memory: int,
                os: str,
                year: int,
                price: int,
                id: int):
        
        #Making it so you cannot assign same ID to multiple computers
        if id in Computer.unique_computers:
            raise ValueError("A computer with ID already exists.")
        else:
            self.description = info
            self.processor_type = processor
            self.hard_drive_capacity = hard_drive
            self.memory = memory
            self.operating_system = os
            self.year = year
            self.price = price
            self.id = id
            Computer.unique_computers.add(id)

    """
    Takes in an int as the new price and updates the price of the associated computer
    """
    def update_price(self, new_price: int):
        self.price = new_price

    """
    Returns the price of the associated computer
    """  
    def get_price(self):
        return self.price

    """
    Takes in a string as the new operating system and updates the type of operation
    system of the associated computer
    """  
    def update_os(self, new_os: str):
        self.operating_system = new_os

    """
    Returns the operating system of the associated computer
    """  
    def get_os(self):
        return self.operating_system

    """
    Returns the year the computer was manufactured of the associated computer
    """  
    def get_year(self):
        return self.year
    
    """
    Returns the ID of the associated computer
    """  
    def get_id(self):
        return self.id
    
    """
    Prints out the full description of the computer.
    """  
    def print(self):
        statement = f"""Description: {self.description}, Processor Type: {self.processor_type}, Hard Drive Capacity: {self.hard_drive_capacity}, Memory: {self.memory}, Operating System: {self.operating_system}, Year Produced: {self.year}, Price: {self.price} """
        return statement