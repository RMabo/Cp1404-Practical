"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

MIN_LENGTH = 2
MAX_LENGTH = 6
SPECIAL_CHARS_REQUIRED = False
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH,
          "characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print(f"Your {len(password)}-character password is valid: {password}")


def is_valid_password(password):
    """Determine if the provided password is valid."""

    # TODO: if length is wrong, return False
    if len(password) > MAX_LENGTH or len(password) < MIN_LENGTH:  # checks if the length of the password is between the min and max length

        return False  # returns false if the length is not between the min and max length

    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    for char in password:
        # TODO: count each kind of character (use str methods like isdigit)
        if char.isdigit():  # isdigit() checks if the string is a digit
            count_digit += 1
        elif char.islower():  # islower() checks if the string is lowercase
            count_lower += 1
        elif char.isupper():  # isupper() checks if the string is uppercase
            count_upper += 1
        elif char in SPECIAL_CHARACTERS:  # checks if the string is in the special characters
            count_special += 1

        # TODO: if any of the 'normal' counts are zero, return False
    if count_lower == 0 or count_upper == 0 or count_digit == 0:  # checks if any of the counts are 0
        return False  # returns false if any of the counts are 0

    # TODO: if special characters are required, then check the count of those
    # and return False if it's zero
    if SPECIAL_CHARS_REQUIRED:  # checks if special characters are required
        if count_special == 0:  # checks if the count of special characters is 0
            return False  # returns false if the count of special characters is 0

    # if we get here (without returning False), then the password must be valid
        return True  # returns true if special characters are required


main()
