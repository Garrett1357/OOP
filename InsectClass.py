import random

class Insect:
    
    def __init__(self,w,l,n): # has to be the first part of all methods
        self.wings = w
        self.legs = l
        self.flight = 0
        self.name = n

    def calc_flight(self):
        self.flight = random.randint(1,10) # So a new random number is generated every time it is called

    def get_miles(self):
        return self.flight
    
    def get_name(self):
        return self.name