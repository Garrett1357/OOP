import InsectClass as IC
def main():
    
    Mosquito = IC.Insect
    Housefly = IC.Insect
    
    Mosquito.calc_flight()
    Housefly.calc_flight()

    print(f"The mosquito can fly up to", {Mosquito.get_miles})
    print(f"The housefly can fly up to", {Housefly.get_miles})

main()