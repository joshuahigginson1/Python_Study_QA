# A file to demonstrate how to configure a  test in python.

# THIS IS THE TESTING FILE! Denoted by the filename_test.py

# Declare Imports ---------------------------------------------------------------------------------------------------

import pytest  # To run a PyTest script, we first need to import and declare the PyTest module.
import double  # We must also reference the file which we want to test.


def test_answer():  # Our tests have to be structured as a function.
    # Here, we are giving the computer our ASSERTION criteria. As a developer, we know explicitly that when we run the
    # calculation 5 * 2, we should only ever get out 10.

    assert double.double_number(5) == 10

"""
The computer will compare our assertion criteria to what is actually output from the operation double.func(5).
If the computer returns True, it means that our program correctly doubled 5. 
If it returns False, it will throw an AssertionError. Your code is not matching your assertion criteria for the test.
"""