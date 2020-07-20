# Declare inputs ----------------------------------------------------------------------------------------------------

import pytest
from programs import list_of_squares

# Declare Tests -----------------------------------------------------------------------------------------------------

def test_squares_ints():
    assert list_of_squares.list_of_squares(3)[3] == 9


def test_squares_zero():
    assert list_of_squares.list_of_squares(0)[0] == 0