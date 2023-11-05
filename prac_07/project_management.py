import csv
import datetime

PROJECTS_FILE = "projects.csv"
MENU = """- (L)oad projects
- (S)ave projects
- (D)isplay projects
- (F)ilter projects by date
- (A)dd new project
- (U)pdate project
- (Q)uit"""


def main():
    """Project management program."""
    print(MENU)
    projects = []
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "L":
            projects = load_projects()
        elif choice == "S":
            pass
        elif choice == "D":
            pass
        elif choice == "F":
            pass
        elif choice == "A":
            pass
        elif choice == "U":
            pass
        else:
            print("Invalid menu choice")

        print(MENU)
        choice = input(">>> ").upper()

    print("Thank you for using custom-built project management software.")


def load_projects():
    """Load projects from file."""
    try:
        projects = []
        with open("projects.txt", "r") as file:
            lines = file.readlines()
            # Skip the first line (header)
            for line in lines[1:]:
                values = line.strip().split('\t')
                name, start_date, priority, cost_estimate, completion_percentage = values
                projects.append([name, start_date, priority, cost_estimate, completion_percentage])
        return projects
    except FileNotFoundError:
        print("No project file found.")
        return []
