"""
Task: Given a string, return the number of times "am" appears in the string...
 ...BUT ONLY WHEN "am" is not followed or preceded by any other LETTERS.

"""


# Functions ------------------------------------------------------------------------------

def amsterdam(input_str, compare):
    input_str = str(f' {input_str.lower()} ')
    compare = str(f' {compare.lower()} ')

    return input_str.count(compare)

