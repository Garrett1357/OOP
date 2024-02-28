import CellphoneClass as phone

my_phone = phone.Cellphone("Apple", "iPhone 13", 999.99)

print("Manufacturer:",my_phone.get_manufact())
print("Model:",my_phone.get_model())
print("Retail Price: $",my_phone.get_retail_price())

#updates

my_phone.set_manufact("Apple")
my_phone.set_model("iPhone 13")
my_phone.set_retail_price(1099.99)

print("/n Updated Phone Details")
print("Manufacturer:", my_phone.get_manufact())
print("Model:", my_phone.get_model())
print("Retail Price: $", my_phone.get_retail_price())