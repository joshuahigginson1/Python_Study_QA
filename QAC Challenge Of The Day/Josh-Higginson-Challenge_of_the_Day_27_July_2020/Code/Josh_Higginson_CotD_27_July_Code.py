"""
Task:

Find all numbers, between 2000 and 3200 (both included), that are divisible by 7, but are not a multiple of 5.
The numbers obtained should be returned on a single lin, separated by commas.

"""

# Functions ------------------------------------------------------------------------------

def seven_not_five(start_var, stop_var, divider_var, not_multiple_var):
    num_list = []

    for n in range(start_var, stop_var):
        if n % divider_var == 0:
            if n % not_multiple_var != 0:
                num_list.append(n)
            else:
                continue
        else:
            continue

    return num_list


# Define Variables -----------------------------------------------------------------------

start = 2000
stop = 3200
divider = 7
not_multiple_of = 5

# Execute Code ---------------------------------------------------------------------------
