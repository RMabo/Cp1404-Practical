"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        # TODO: this line
        if result < 0: # if result is less than 0
            print("Please enter a positive integer")
            result = int(input("Enter a valid integer: "))
        else: # if result is greater than 0
            is_finished = True
    except ValueError:  # ValueError is raised when the input is not an integer
        print("Please enter a valid integer.")
print(f"Valid result is: {result}".strip())
