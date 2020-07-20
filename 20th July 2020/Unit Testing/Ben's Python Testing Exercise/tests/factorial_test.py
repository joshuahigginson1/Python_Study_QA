# Declare inputs ----------------------------------------------------------------------------------------------------

import pytest
from programs import factorial


# Declare Tests -----------------------------------------------------------------------------------------------------

def test_factorial_ints():
    assert factorial.fact(3) == 6


def test_factorial_zero():
    assert factorial.fact(0) == 1
