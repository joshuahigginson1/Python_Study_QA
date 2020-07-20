# Write a piece of code that counts how many instances of a particular item are in a list.
# For example, if we want to find out how many letter 'a's are there in a particular word, we can do so.

# Describe Functions -------------------------------------------------------------------------------------------------


def count(sequence, item):
    sum = 0
    for n in sequence:
        if n == item:
            sum += 1
    return sum


# Declare Variables --------------------------------------------------------------------------------------------------

sequence_of_numbers = [0, 0, 0]
item_to_count = 0

# Execute Code ------------------------------------------------------------------------------------------------------

