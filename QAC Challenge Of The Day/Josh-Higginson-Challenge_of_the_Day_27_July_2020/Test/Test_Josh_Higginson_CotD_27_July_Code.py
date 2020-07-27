"""

TEST CODE

Task:

Find all numbers, between 2000 and 3200 (both included), that are divisible by 7, but are not a multiple of 5.
The numbers obtained should be returned on a single lin, separated by commas.
"""

# Imports --------------------------------------------------------------------------------

import pytest

import random

from Code import Josh_Higginson_CotD_27_July_Code

# Variables --------------------------------------------------------------------------------

start = Josh_Higginson_CotD_27_July_Code.start
stop = Josh_Higginson_CotD_27_July_Code.stop
divider = Josh_Higginson_CotD_27_July_Code.divider
not_multiple_of = Josh_Higginson_CotD_27_July_Code.not_multiple_of


# Tests ----------------------------------------------------------------------------------

def test_for_lower():
    test_set = Josh_Higginson_CotD_27_July_Code.seven_not_five(start, stop, divider, not_multiple_of)
    assert min(test_set) >= start


def test_for_higher():
    test_set = Josh_Higginson_CotD_27_July_Code.seven_not_five(start, stop, divider, not_multiple_of)
    assert max(test_set) <= stop


def test_for_number():
    test_set = Josh_Higginson_CotD_27_July_Code.seven_not_five(start, stop, divider, not_multiple_of)
    for n in test_set:
        assert isinstance(n, int)


def test_for_divider():
    test_set = Josh_Higginson_CotD_27_July_Code.seven_not_five(start, stop, divider, not_multiple_of)
    for test in range(20):
        assert random.choice(test_set) % divider == 0


def test_for_not_multiple():
    test_set = Josh_Higginson_CotD_27_July_Code.seven_not_five(start, stop, divider, not_multiple_of)
    for test in range(20):
        assert random.choice(test_set) % not_multiple_of != 0