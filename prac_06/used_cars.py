"""
CP1404/CP5632 Practical
"""

from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car(180, 'car')
    my_car.drive(30)
    print(f"fuel = {my_car.fuel}, odometer = {my_car.odometer}")
    print(my_car)
    print(f"fuel = {my_car.fuel}, odometer = {my_car.odometer}")
    print("Car {self.fuel}, {self.odometer}".format(self=my_car))
    print(f"Car {my_car.fuel}, {my_car.odometer}")
    limo = Car(100, 'limo')
    limo.add_fuel(20)
    print(f"limo fuel = {limo.fuel}")
    limo.drive(115)
    print(f"limo odometer = {limo.odometer}")
    print(limo)


main()
