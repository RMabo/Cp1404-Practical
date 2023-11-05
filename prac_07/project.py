"""Practical 07 project - CP1404/CP5632"""


class Project:

    def __init__(self, name="", start_date="", priority="", cost_estimate="", percent_complete=""):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.percent_complete = percent_complete

    def __str__(self):
        """Represent project object as a string."""
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: ${self.cost_estimate}," \
               f"completion: {self.percent_complete}%"

    def __repr__(self):
        """Represent project object as a string."""
        return f"{self.name}\t{self.start_date}\t{self.priority}\t{self.cost_estimate}\t{self.completion_percentage}"

    def __lt__(self, other):
        """Less than comparison."""
        return self.start_date < other.start_date

    def is_complete(self):
        """Determine if a project is complete."""
        return self.percent_complete == 100
