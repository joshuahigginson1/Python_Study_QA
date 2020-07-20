# Write a piece of code that counts how many instances of a particular item are in a list.

# Declare Imports ---------------------------------------------------------------------------------------------------

import pytest  # Import PyTest module in order to run tests.

from Program import count  # Import our original program into the test script.


# Define Tests ------------------------------------------------------------------------------------------------------

def test_count_zeros():  # Check if the function works for integers.
    assert count.count([0, 0, 0], 0) == 3


def test_count_string():  # Check if the function works for strings.
    assert count.count(["a", "a", "a"], "a") == 3
