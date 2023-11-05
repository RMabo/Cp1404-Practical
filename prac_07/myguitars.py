"""
CP1404 Practical 07 - guitar Classes
"""
import csv
from prac_07.guitar import Guitar

def main():
    """Guitar program"""
    guitars = []
    print("My guitars!")
    get_guitar_file(guitars)
    get_updated_guitar_file(guitars)
    display_guitars(guitars)


def get_guitar_file(guitars):
    """Get guitars from file"""
    in_file = open("guitars.csv", "r")
    for line in in_file:
        parts = line.strip().split(",")
        guitars.append(parts)
    in_file.close()


def get_updated_guitar_file(guitars):
    """Get guitars from user and add to file"""
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitars.append([name, year, cost])
        print(f"{name} ({year}) : ${cost:,.2f} added.")
        name = input("Name: ")
    out_file = open("guitars.csv", "w")
    for guitar in guitars:
        print(",".join(str(guitar)), file=out_file)
    out_file.close()


def display_guitars(guitars):
    """Display guitars from file and sort by year"""
    guitars.sort()
    for i, guitar in enumerate(guitars, 1):
        vintage_string = ""
        if guitar.is_vintage():
            vintage_string = " (vintage)"
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")


main()
