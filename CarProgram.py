from CarClass import Car as C

def main():
    car = C(2020, "Kia")  #Establishes car instance
    print(car)

#accelerate 5 times
    print("Accelerating:")
    for x in range(5):
        car.accelerate()
        print(f"Current speed: {car.get_speed()}") #returns current speed before looping


#brake 5 times
    print("\nBraking:")
    for x in range(5):
        car.brake()
        print(f"Current speed: {car.get_speed()}") #returns current speed before looping

main()


#Garrett Austin