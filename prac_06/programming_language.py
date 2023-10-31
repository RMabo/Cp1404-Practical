"""
CP1404/CP5632 Practical
"""


class ProgrammingLanguage:
    """Represent a Programming Language object"""

    def __init__(self, name, typing, reflection, year):
        """Initialise a ProgrammingLanguage instance"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):  # added __str__ method
        """Return string representation of ProgrammingLanguage object"""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):  # added is_dynamic method
        """Return True if programming language is dynamically typed, False otherwise"""
        return self.typing == "Dynamic"
