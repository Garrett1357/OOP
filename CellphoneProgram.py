from CellphoneClass import Cellphone as phone

my_phone = phone()

print("Original Phone Details\n")
print("Manufacturer:",my_phone.get_manufact())
print("Model:",my_phone.get_model())
print("Retail Price: $",my_phone.get_retail_price(),"\n")

#updates

my_phone.set_manufact()
my_phone.set_model()
my_phone.set_retail_price()

print("Updated Phone Details\n")
print("Manufacturer:", my_phone.get_manufact())
print("Model:", my_phone.get_model())
print("Retail Price: $", my_phone.get_retail_price())