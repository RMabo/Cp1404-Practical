"""Use 2 functions (NOT one!) for converting Celsius to Fahrenheit and vice versa.
Important: Remember SRP - functions should do one thing, so these should be simple calculation functions.
Do not get user input or print output in the functions - do those things outside.
"""

MENU = """\n C - Convert Celsius to Fahrenheit\n F - Convert Fahrenheit to Celsius\n Q - Quit"""


def main():
    """ Temperature Conversion"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = convert_celsius_to_fahrenheit(celsius)
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = convert_fahrenheit_to_celsius(fahrenheit)
            print("Result: {:.2f} C".format(celsius))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
        print("Thank you.")


def convert_fahrenheit_to_celsius(fahrenheit):
    """Convert fahrenheit to celsius"""
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


def convert_celsius_to_fahrenheit(celsius):
    """Convert celsius to fahrenheit"""
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


main()
