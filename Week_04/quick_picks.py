"""
CP1404/CP5632 Practical
Write a program that asks the user how many "quick picks" they wish to generate. The program then generates that many
lines of output. Each line consists of 6 random numbers between 1 and 45.
These values should be stored as CONSTANTS.

Each line (quick pick) should not contain any repeated number.
Each line of numbers should be displayed in sorted (ascending) order.
Study the formatting below so that numbers align neatly.

"""

import random

MINIMUM = 1
MAXIMUM = 45
NUMBERS_PER_LINE = 6

user_input = int(input("How many quick picks? "))
for i in range(user_input):
    quick_pick = []
    for j in range(NUMBERS_PER_LINE):
        number = random.randint(MINIMUM, MAXIMUM)  # Generate random number
        while number in quick_pick:
            number = random.randint(MINIMUM, MAXIMUM) # Generate random number
        quick_pick.append(number)  # Add number to quick pick
    quick_pick.sort()  # Sort quick pick
    print(" ".join("{:2}".format(number) for number in quick_pick))  # prints the quick pick
