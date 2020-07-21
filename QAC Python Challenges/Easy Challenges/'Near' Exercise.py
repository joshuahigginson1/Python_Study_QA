"""

Task: When given two strings of letters,
determine whether the second can be made from the first by removing one letter.

The remaining letters must stay in the same order.

near ("reset", "rest") => true
near ("dragoon", "dragon") => true
near ("eave", "leave") => false
near ("sleet", "lets") => false

Dev Notes:

1. Convert each string to list.

delete each character index, and compare that that to the given second string.

for loop to do this.

If statement to return true or false.

"""


# Define Functions ---------------------------------------------------------------------------------------------------

def near_function(first, second):
    first_string_list = list(first)
    second_string_list = list(second)
    first_string_list_destroy = first_string_list

    for letters in range(len(first_string_list)):
        first_string_list_destroy = list(first_string_list)  # Without converting to a new list, python will share ID.
        first_string_list_destroy.pop(letters)  # Delete letter from that particular index.

        if first_string_list_destroy == second_string_list:
            return True

        else:
            continue


# Declare Variables --------------------------------------------------------------------------------------------------

first_string = "Bananas"
second_string = "Banana"

# Execute Code -------------------------------------------------------------------------------------------------------

if near_function(first_string, second_string):
    print(f"The word: {second_string} fits into the word: {first_string}")

else:
    print(f"The word: {second_string} does NOT fit into the word: {first_string}")
