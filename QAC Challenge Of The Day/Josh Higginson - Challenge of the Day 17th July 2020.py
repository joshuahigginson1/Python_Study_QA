"""
Given an integer n, write a python function which returns a times table grid for all the integers between 1 and n.
The grid should be separated by tabs and new lines.

Plan: We use nested for loops.
To print the numbers, we add calculations to a list..

n = 3

    [1, 2, 3, 4, ..., n-2, n-1, n]
    [2, 4, 6, 8, ..., 2(n-2), 2(n-1), 2n]
    [3, 6, 9, 12, ..., 3(n-2), 3(n-1), 3n]
    [4, 8, 12, 16, ..., 4(n-2), 4(n-1), 4n]
    [n-2,
    [n-1,
    [n, 2n, 3n, 4n, ..., (n-2)(n-2), (n-1)(n-1), n^2]

You have two moving sliders, ranging from 1 to n.
When x pointer hits n, then y pointer adds 1.

To format our grid, we first need to convert our list into a string. For this, we can use replace() and strip().
"""


# Define Functions ---------------------------------------------------------------------------------------------------

def grid_formatting(list_of_integers):  # Takes a list of integers as in input, and returns a formatted string.
    format_list = str(list_of_integers)  # Converts the entire list to one long string.
    format_list = format_list.replace(', ', '\t')  # Replaces each comma character within the given string with a tab.
    format_list = format_list.strip('[]')  # Removes square brackets.

    return format_list


def user_input():  # Error prevention for a user input to the program.
    repeat = True
    while repeat:

        input_value = input("Please enter a positive integer: ")  # Gets a value from user.
        if input_value.lower() == 'q':  # Quits the program if the user presses q.
            quit()

        else:
            try:
                output = int(input_value) + 1  # We add one, because python indexes from '0'
                if output <= 1:
                    raise ValueError  # If this value is not a positive integer, there will be no grid drawn!
            except:
                print("Please enter an integer value! You can quit the program at any time by pressing q.")
                continue

        repeat = False
        return output


# Define Procedures --------------------------------------------------------------------------------------------------


def times_table_grid(multiplier):
    integer_list = []

    x_index_pointer = 0
    y_index_pointer = 0

    for y_index_pointer in range(1, multiplier):
        for x_index_pointer in range(1, multiplier):
            # print(f"the x index pointer is {x_index_pointer}")  # Used for debugging.
            # print(f"the y index pointer is {y_index_pointer}")  # Used for debugging.
            integer_list.append(x_index_pointer * y_index_pointer)  # Multiplies pointers, appends them to a list.

        # print(integer_list)  # You could leave it here, but wouldn't have fancy formatting.
        print(grid_formatting(integer_list))  # Outputs formatted row to the terminal.
        integer_list.clear()  # If we don't clear the list, then the previous iteration's data will persist.


# Initialise variables -----------------------------------------------------------------------------------------------


# Execute Code -------------------------------------------------------------------------------------------------------

print("Welcome to the times table grid program! You can quit by typing 'Q'")
input_num = user_input()

times_table_grid(input_num)
