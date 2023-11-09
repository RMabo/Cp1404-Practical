"""
CP1404/CP5632 Practical - Car class example.
"""


class Car:
    """Represent a Car object."""

    def __init__(self, fuel=0, name=""):  # added name parameter
        """Initialise a Car instance.
        fuel: float, one unit of fuel drives one kilometre
        name: string, name of car
        """
        self.fuel = fuel
        self.odometer = 0
        self.name = name  # added name attribute

    def __str__(self):  # added __str__ method
        """Return string representation of Car object"""
        return f"{self.name}, fuel={self.fuel}, odometer={self.odometer}"

    def add_fuel(self, amount):
        """Add amount to the car's fuel."""
        self.fuel += amount

    def drive(self, distance):  # added drive method
        """Drive the car a given distance if it has enough fuel or drive until fuel runs out return the distance actually driven"""
        if distance > self.fuel:  # if distance is more than fuel
            distance = self.fuel  # distance is equal to fuel
            self.fuel = 0  # fuel is equal to 0
        else:
            self.fuel -= distance  # subtract distance from fuel
        self.odometer += distance  # add distance to odometer
        return distance  # return distance
