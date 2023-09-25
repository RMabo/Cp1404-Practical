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
    print(MENU)
    score = float(input("Enter score: "))
    valid_score(score)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            # score = float(input("Enter score: "))
            print("You have validated your score")
        elif choice == "P":
            print(score_result(score))
        elif choice == "S":
            print(stars(score))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def valid_score(score):
    if score < 0 or score > 100:
        print("Invalid score.Please enter a valid score")
    else:
        return score


def score_result(score):
    """ Calculate score result"""
    if score >= 90:
        print("Excellent")
    elif 50 <= score <= 89:
        print("Passable")
    else:
        print("Bad")


def stars(score):
    """Calculate stars"""
    number_stars = int(score / 10)
    return "*" * number_stars


main()
