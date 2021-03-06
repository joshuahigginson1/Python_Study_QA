"""
I have a function called `string_gen()` that will return a random 5-character-long string of lowercase letters.
 Write some tests for this function.

To reiterate, the output should always be:

A string, 5 characters long, and comprised of lowercase letters.

"""

# Declare Imports ----------------------------------------------------------------------------------------------------

import pytest  # Import PyTest to run tests on code.

import string_gen  # Replace with Harry's file name.


# Define Tests ------------------------------------------------------------------------------------------------------

def test_string():
    for _ in range(20):
        assert isinstance(string_gen.string_gen(), str)


def test_five_chars():
    for _ in range(20):
        assert len(string_gen.string_gen()) == 5


def test_lower_case():
    for _ in range(20):
        assert string_gen.string_gen().islower()
