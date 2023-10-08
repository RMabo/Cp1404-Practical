"""
CP1404/CP5632 Practical
Data file -> lists program
Remember to commit these before modifying them any further.
Study the starter code and run it. There are comments and print calls to show you what's happening.

The code reads the file data and processes it into the parts variable, but we want the get_data function to return the
data as a list of lists (nested list), like:
[['CP1401', 'Ada Lovelace', 192],['CP1404', 'Alan Turing', 98]]
Modify the function so that it does this.

Currently, main just prints data. Add a new function to display subject details that produces something like the
following:
"""

FILENAME = "subject_data.txt"


def main():
    """Read subject data and display data."""
    data = get_data()
    print(data)
    display_subject_details(data)


def get_data(): # added get_data function
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)  # opens the file
    parts = []  # empty list
    for line in input_file:
        line = line.strip()  # removes the \n
        parts.append(line.split(','))  # splits the line by the comma
    input_file.close()  # closes the file
    return parts  # returns the list


def display_subject_details(datas): # added display_subject_details function
    """Display subject details"""
    for subject_data in datas: # for each subject data in the list
        print(f"{subject_data[0]} is taught by {subject_data[1]} and has {subject_data[2]} students")  # prints the subject details
    return sorted(datas, key=lambda x: x[2], reverse=True)  # sorts the list by the number of students


main()
