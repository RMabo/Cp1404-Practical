"""
write a program that asks the user for a password, with error-checking to repeat if the password doesn't meet a minimum
length set by a variable. The program should then print asterisks as long as the word.
Example: if the user enters Pythonista (10 characters), the program should print **********.
"""

MINIMUM_LENGTH = 10


def main():
    """Get password and print asterisks"""
    password = input("Password: ")
    while len(password) < MINIMUM_LENGTH:
        print(f"Invalid password! Must be {MINIMUM_LENGTH} characters long")
        password = input("Password: ")
    print_asterisks(password)


def print_asterisks(password):
    """Print asterisks"""
    for i in range(len(password)):
        print("*", end="")


main()
