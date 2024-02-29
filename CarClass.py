class Car:

    def __init__(self,year_model,make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0 #Initilizes speed to 0

    #accelerate function
    def accelerate(self):
        self.__speed += 5 #increases vehicle speed by 5 when called
    
    #Brake function
    def brake(self):
        self.__speed -= 5

    def get_speed(self): #passes speed to program
        return self.__speed
    
    def __str__(self): # Allows the Make/Model to be printed by the __str__ method
        return f"Year Model: {self.__year_model}, Make: {self.__make}, Current Speed: {self.__speed}"
    
    #Garrett Austin