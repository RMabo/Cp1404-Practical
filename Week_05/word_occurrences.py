"""
CP1404 Practical 05
word_occurrences.py
"""

"""
Write a program to count the occurrences of words in a string. The program should ask the user for a string, 
then print the counts of how many of each word are in the string.
The output should look like this (depending on user input):

Hints: use a dictionary where the keys are the words and the values are the counts; when you find a word, check if it's 
in the dictionary...

Notice that the sample output is sorted.
Only after you have the program working, make your program do this sorting.

Now align the outputs so the numbers are in one nice column. You will need to find the longest word in the list first.
Then you can use f-string formatting and a variable width. This can be done with another {} placeholder, like in this 
example:

This formats the first placeholder value, thing, with a width of width then prints a literal = then the value of other_thing.
Your output should then look something like:
Now that you've read the instructions, remember to record your time estimate in your docstring.

"""



def main():
    """Count the occurrences of words in a string"""
    word_to_count = get_word_to_count() # gets the dictionary
    word = input("Enter a string: ")
    word = word.split() # splits the string into a list
    for word in word:
        word_to_count[word] = word_to_count.get(word, 0) + 1 # counts the number of times a word occurs
    word = list(word_to_count.keys())
    word.sort()
    max_length = max((len(word) for word in word)) # finds the longest word
    for word in word:
        print(f"{word:{max_length}} : {word_to_count[word]}") # prints the word and the number of times it occurs


def get_word_to_count():
    """dictionary of words and counts"""
    word_to_count = {} # empty dictionary
    return word_to_count


main()





