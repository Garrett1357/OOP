import InsectClass as IC

def main():
    
    Mosquito = IC.Insect(2,4,'Mosquito')
    Housefly = IC.Insect(2,4,'Housefly')
    
    Mosquito.calc_flight() # Needs to be called for the calculation to happen
    Housefly.calc_flight()

    print(f"The {Mosquito.get_name()} can fly up to", Mosquito.get_miles(),"miles.")  # Call get_miles() on Mosquito instance
    print(f"The {Housefly.get_name()} can fly up to", Housefly.get_miles(),"miles.")  # Call get_miles() on Housefly instance

main()