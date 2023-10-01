"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task

"""

# Write code that asks the user for their name, then opens a file called "name.txt" and writes that name to it.
# Remember to close your file.

name = input("Enter your name: ")  # get name
filename = open("name.txt", "w")  # open file
print(name, file=filename)  # print name to file
filename.close()  # close file

# (In the same file, but as if it were a separate program) Write code that opens "name.txt" and reads the name (as above)
# then prints,
# "Your name is Bob" (or whatever the name is in the file).

filename = open("name.txt", "r")  # open file
name = filename.read().strip()  # read name
print("Your name is", name)  # print name
filename.close()  # close file

# Now write a fourth block of code that prints the total for all lines in numbers.txt or a file with any number of numbers.

filename = open("numbers.txt", "r")  # open file
total = 0  # set total to 0
for line in filename:  # for each line in file
    number = int(line)  # convert line to int
    total += number  # add number to total
print(total)  # print total
filename.close()  # close file
