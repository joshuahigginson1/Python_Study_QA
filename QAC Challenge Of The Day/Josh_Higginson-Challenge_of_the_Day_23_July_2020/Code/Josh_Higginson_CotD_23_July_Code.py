"""
Task: Write a function that accepts a seq of whitespace separated words as a string input, sorts
each item alphanumerically and removes any duplicate items.

Return the result as a string.

Dev Notes:


"""


# Functions ------------------------------------------------------------------------------

def word_sorter(string):
    string = str(string)
    string_input = list(set(string.split(" ")))
    sorted_input = sorted(string_input, key=str.lower)
    output = " ".join(sorted_input)

    return output


print(word_sorter("9oodworm 9pple 3offee 6imple 8hiny 56hellshock 3ardvark"))
