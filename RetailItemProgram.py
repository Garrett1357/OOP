from RetailItemClass import RetailItem as RI

item1 = RI("Jacket", 12, 59.95)
item2 = RI("Designer Jeans", 40, 34.95)  #creates three RetailItem objects and stores data
item3 = RI("Shirt", 20, 24.95)
item_list = [item1,item2,item3] #generates list for printing

for item in item_list:
    print(f"Description: {item.description}, Units: {item.units}, Price: ${item.price}\n")