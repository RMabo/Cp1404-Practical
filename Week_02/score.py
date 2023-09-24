"""
CP1404/CP5632 - Practical 02
Main function should ask the user for their score and print the result.
Write a new function that takes in the user's score as a parameter and returns the result to be printed.
Follow SRP: The function should not print it.

Now add a new part to the bottom of your main function that generates a random score and prints the result.
You do NOT need to write a different function to determine the result for the random score.
If you've written your new function properly, you can use it.
If you've breached SRP, then you'll see that you can't.

"""
import random


def main():
    """"Determine score status"""
    score = float(input("Enter score: "))
    random_score = random.randint(0, 100)
    print(score_result(score))


def score_result(score):
    """Calculate score result"""
    if score < 0 or score > 100:
        return "Invalid score"
    else:
        if score >= 90:
            return "Excellent"
        elif score >= 50:
            return "Passable"
        else:
            return "Bad"



main()
