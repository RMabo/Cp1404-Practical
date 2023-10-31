"""
CP1404 Practical 05
hex_colours.py
"""

"""
Based on the state name example program above, create a program that allows you to look up hexadecimal colour codes like 
those at http://www.color-hex.com/color-names.html

Use a constant dictionary of about 10 colour names and write a program that allows a user to enter a name and get the 
code, e.g., entering AliceBlue (or aliceblue - make it case-independent) should show #f0f8ff.
Entering an invalid colour name should not crash the program.
Allow the user to enter names until they enter a blank one to stop the loop.

One very useful skill for programmers, and students, is the ability to estimate well.
For each of the following exercises, read the instructions then estimate how long you think the task will take to complete.
Record your estimation in the docstring at the top of your solution.
Set a timer when you start the work.
Then, when you finish, record how long it actually took in the same place.
"""

# Version 01
COLOUR_CODES = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "AntiqueWhite1": "#ffefdb",
                "AntiqueWhite2": "#eedfcc", "AntiqueWhite3": "#cdc0b0", "AntiqueWhite4": "#8b8378",
                "aquamarine1": "#7fffd4", "aquamarine2": "#76eec6", "aquamarine4": "#458b74",
                "azure1": "#f0ffff", "azure2": "#e0eeee", "azure3": "#c1cdcd", "azure4": "#838b8b",
                "beige": "#f5f5dc", "bisque1": "#ffe4c4", "bisque2": "#eed5b7", "bisque3": "#cdb79e"}

colour_name = input("Enter a colour name: ")  # Get user input
while colour_name != "":  # while colour name is not blank
    if colour_name in COLOUR_CODES:  # if colour name is in colour codes
        print(colour_name, "is", COLOUR_CODES[colour_name])  # print colour name and colour code
    else:  # if colour name is not in colour codes
        print("Invalid colour name")  # print invalid colour name
    colour_name = input("Enter a colour name: ")  # Get user input



# Version 02 with functions & exceptions
def main(): # main function
    """Get colour name and colour code"""
    colour_name_to_code = get_colour_name_to_code()
    colour_name = input("Enter a colour name: ")  # Get user input
    while colour_name != "":  # while colour name is not blank
        try:
            print(colour_name, "is", colour_name_to_code[colour_name])  # print colour name and colour code
        except KeyError:
            print("Invalid colour name")
        colour_name = input("Enter a colour name: ")  # Get user input


def get_colour_name_to_code(): # get colour name to code
    """dictionary of colour names and colour codes"""
    COLOUR_CODES = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "AntiqueWhite1": "#ffefdb",
                    "AntiqueWhite2": "#eedfcc", "AntiqueWhite3": "#cdc0b0", "AntiqueWhite4": "#8b8378",
                    "aquamarine1": "#7fffd4", "aquamarine2": "#76eec6", "aquamarine4": "#458b74",
                    "azure1": "#f0ffff", "azure2": "#e0eeee", "azure3": "#c1cdcd", "azure4": "#838b8b",
                    "beige": "#f5f5dc", "bisque1": "#ffe4c4", "bisque2": "#eed5b7", "bisque3": "#cdb79e"}
    return COLOUR_CODES


main()
