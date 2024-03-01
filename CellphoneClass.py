class Cellphone:
    def __init__(self):
        self.__manufact = 'Apple'
        self.__model = 'iPhone 12'
        self.__retail_price = '799.99'

    def set_manufact(self):
        self.__manufact = input("New Manufacturer: ")

    def set_model(self):
        self.__model = input("New Model: ")

    def set_retail_price(self):
        self.__retail_price = input("New Price: ")

    def get_manufact(self):
        return self.__manufact
    
    def get_model(self):
        return self.__model
    
    def get_retail_price(self):
        return self.__retail_price