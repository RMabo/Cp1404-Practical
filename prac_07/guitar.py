"""
CP1404 Practical 07 - guitar Classes
"""

CURRENT_YEAR = 2023


class Guitar:
    """Represent a Guitar object."""

    def __init__(self, name="", year=0, cost=0):  # added __init__ function
        """Initialise a Guitar instance.

        name: string, name of guitar
        year: int, year guitar was made
        cost: float, cost of guitar
        """
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):  # added __str__ function
        """Return string representation of Guitar object"""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):  # added get_age function
        """Determine how old the guitar is in years"""
        age = CURRENT_YEAR - self.year
        return age

    def is_vintage(self):  # added is_vintage function
        """Determine if guitar is vintage or not"""
        return self.get_age() >= 50  # calls get_age function to determine if guitar is 50 or more years old

    def __lt__(self, other):  # added __lt__ function
        """Less than function to sort guitars by year"""
        return self.year < other.year

    def __eq__(self, other):  # added __eq__ function
        """Equal function to sort guitars by year"""
        return self.year == other.year
