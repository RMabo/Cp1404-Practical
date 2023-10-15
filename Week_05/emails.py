"""
CP1404 Practical 05
emails.py

Write a program that stores users' emails (unique keys) and names (values) in a dictionary.
Ask the user for their email until they enter a blank one.
Use a separate function to extract a name from the email as in the example below.
You should find the following methods useful: split, join, title.

Notice the prompt to check if the name is correct: Y/n
This is used in console programs (like in Linux etc.) so you can just press Enter to accept the default of (Y)es.
Example from Linux:

> sudo apt-get upgrade
...
After this operation, 267 kB of additional disk space will be used.
Do you want to continue? [Y/n] blah
Abort.
In our program, if the user does not press Enter or Y, then ask for their name.
Once you have stored all the emails and names, just loop through the dictionary (use the items method) and print them out.
"""


def main():
    """Get user email and name"""
    email_to_name = get_email_to_name() # gets the dictionary
    email = input("Email: ")
    while email != "":
        name = get_name_from_email(email)
        correct_name = input(f"Is your name {name}? (Y/n) ").upper() # asks the user if the name is correct
        if correct_name != "Y" and correct_name != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")
    for email, name in email_to_name.items(): # loops through the dictionary
        print(f"{name} ({email})") # prints the name and email


def get_email_to_name():
    """dictionary of emails and names"""
    email_to_name = {} # empty dictionary
    return email_to_name # empty dictionary


def get_name_from_email(email):
    """Get name from email"""
    prefix = email.split('@')[0] # splits the email into a list
    parts = prefix.split('.') # splits the prefix into a list
    name = " ".join(parts).title() # joins the parts of the prefix and capitalises the first letter of each word
    return name


main()


