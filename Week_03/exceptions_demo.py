"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur? When the numerator & denominator is not a valid integer
2. When will a ZeroDivisionError occur?  If Denominator is equal to 0
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
yes, by using exception - based error checking. Or to avoid the
ZeroDivisionError by checking if the denominator is 0 before performing the division operation
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")