'''
Create a program which validates an ISBN.

An ISBN is an identifier for books. It is a thirteen-digit code, with the last number acting as a checksum value.

To calculate the last number of an ISBN, a mathematical rule is applied:

- The first 12 digits are fixed.
- Starting at index 1, if the index is odd - add it, and if the index is even – multiply the digit by three then add it.
- From the sum, find the remainder after dividing by 10.
- 10 minus the remainder gives us the check digit.

Therefore, the following algebra wold give us the check digit
( 10 – (( x1 + 3x2 + x3 + 3x4 + x5 + 3x6 + x7 + 3x8 + x9 + 3x10 + x11 + 3x12 ) % 10))

For ISBN: 978-0-306-40615-? The following check would happen:
9 +  3*7 +   8 +   3*0 +   3 +   3*0 +   6 +  3*4 +   0 +  3*6 + 1 +  3*5 = 93

ISBN to a variable.
Check that the ISBN is valid.
If index is even, we multiply the number by 3. -> We can use if statement - if index % 2 = 0, then multiply by three.
Use enumerate. 

For an ISBN to be valid, it must:
Consist of 13 characters.
Characters must be numbers only.
'''

# Imports -----------------------------------------------------------------------------------------------------------

import time  # Used for the sleep() function.


# Define functions --------------------------------------------------------------------------------------------------

def run_program(run_again_input):
    print("\nWould you like to check an ISBN? You can quit at any time by pressing 'q'.")

    while run_again_input:

        try:
            run_check = input("y, n, or q: ")

            if run_check.lower() == 'q' or run_check.lower() == 'n':
                run_again_input = False
                break

            elif run_check.lower() == 'y':
                run_again_input = True
                break

            else:
                raise Exception()
        except:
            print("\n Please enter a valid user input.")
            continue

    return run_again_input


def isbn_validity_test(isbn):  # Runs the ISBN checksum test.
    counter_value = 0

    for index_counter, isbn_number in enumerate(isbn, 1):  # Loop through each character with for statement.

        if index_counter == 13:
            break

        elif index_counter % 2 == 0:  # If index_counter is even...
            counter_value = counter_value + (3 * int(isbn_number))  # ...multiply by 3 and add to counter_value.

        else:  # If index_counter is odd...
            counter_value = counter_value + int(isbn_number)  # ...add to counter_value.

    checksum_remainder = counter_value % 10  # Find the remainder after dividing by 10.
    check_digit = 10 - checksum_remainder  # 10 minus the remainder gives us the check digit.  #

    return check_digit


def user_input_test():  # Takes user input and checks it is a valid ISBN.

    valid_user_input = False

    while not valid_user_input:  # While there is an invalid user input...
        try:
            isbn = isbn_strip(input("\nPlease enter an ISBN: "))  # Takes input from user.

            if isbn.lower() == 'q':  # User can quit at any time by typing q.
                valid_user_input = True

            elif len(isbn) == 13 and isbn.isnumeric():  # Requirements for a valid isbn.
                valid_user_input = True  # Break out of loop if isbn fits criteria.

            else:
                raise Exception()  # Raise an exception if user input is not a 13 digit integer.
        except:
            print("\nPlease enter a 13 digit integer.")
            continue  # Go back to top of while loop.

    if isbn.lower() == 'q':  # User can quit at any time by typing q.
        print("\n Thank you for using the program. Goodbye!")
        quit()
    else:
        return isbn  # Returns isbn as string.


def isbn_strip(isbn):
    values_to_strip = ['-', ' ', '_', "."]  # List of values to strip from isbn variable.

    for characters in values_to_strip:
        isbn = isbn.replace(characters, "")  # Removes characters from the isbn variable, for every value in strip list.

    return isbn


# Define procedures -------------------------------------------------------------------------------------------------


def checksum_comparison(stripped_isbn, check_digit):
    if int(stripped_isbn[-1]) == check_digit:
        print(f"\nThe ISBN: {stripped_isbn} is a valid ISBN! The checksum is {check_digit}")

    else:
        print(f"\nThe ISBN: {stripped_isbn} is not a valid ISBN! The checksum is {check_digit}")


# Initialise Variables ----------------------------------------------------------------------------------------------
user_isbn = None
user_check_digit = None
runtime = True  # Establishes runtime loop.

# Execute Code ------------------------------------------------------------------------------------------------------

print("Welcome to Josh's ISBN validity check program.")
time.sleep(0.5)

while runtime:

    runtime = run_program(runtime)
    if not runtime:
        break

    user_isbn = user_input_test()  # Gets the ISBN from the user.
    user_check_digit = isbn_validity_test(user_isbn)  # Returns ISBN check digit.
    checksum_comparison(user_isbn, user_check_digit)  # Compares check digits to last number of ISBN.

time.sleep(0.5)
print("\nThank you for using the program. Goodbye!")
quit()
