class Cellphone:
    def __init__(self,ma,mn,rp):
        self.__manufact = ma
        self.__model = mn
        self.__retail_price = rp

    def set_manufact(self,ma):
        ma = input('What is the manufacturer? ')

    def set_model(self,mn):
        mn = input('What is the model? ')

    def set_retail_price(self, rp):
        rp = input('What is the retail price? ')   

    def get_manufact(self):
        return self.__manufact
    
    def get_model(self):
        return self.__model
    
    def get_retail_price(self):
        return self.__retail_price