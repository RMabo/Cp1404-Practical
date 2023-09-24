"""
Write a complete Python program following the standard structure that uses a main and other functions.
Use a main menu following the standard menu pattern.

The menu should have four separate options:

(G)et a valid score (must be 0-100 inclusive)
(P)rint result (copy or import your function to determine the result from score.py)
(S)how stars (this should print as many stars as the score)
(Q)uit
Handle each of these (except quit) separately, and consider how you can reuse your functions. In main(), before the menu loop, get the valid score.
When the user quits, say some kind of "farewell".
"""

""" Choice menu"""
MENU = "(G)- Get a valid score \n(P)- Print result\n (S)- Show stars\n(Q)- Quit"


def main():
    """Determine score status"""
    score = float(input("Enter score: "))
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = float(input("Enter score: "))
        elif choice == "P":
            print(score_result(score))
        elif choice == "S":
            print(stars(score))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


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


def stars(score):
    """Calculate stars"""
    for i in range(score):
        print("*", end="")
    print()


main()
