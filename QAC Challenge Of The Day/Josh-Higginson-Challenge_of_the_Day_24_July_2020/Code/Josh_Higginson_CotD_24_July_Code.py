"""
Task:

Write a function that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program: 9 Then, the output should be: 11106 (i.e. 9+99+999+9999)

Dev Notes:


"""

# Imports --------------------------------------------------------------------------------


# Functions ------------------------------------------------------------------------------

def cotd_24_july(input):

    list_of_numbers = []

    str_cat = str(input)  # Makes sure that the input to the function is a string.
    str_sum = str(f'{str_cat} {str_cat}{str_cat} {str_cat}{str_cat}{str_cat} {str_cat}{str_cat}{str_cat}{str_cat}')

    #  ^ Use of f string formatting syntax, quicker than learning how to use regular expressions! ^

    str_list = str_sum.split(" ")  # Split the long list of new strings by whitespace.

    for string in str_list:
        list_of_numbers.append(int(string))  # Convert each string object in str_list to an int + append to new list.

    output = sum(list_of_numbers)  # Sum all numbers in the list.

    return output