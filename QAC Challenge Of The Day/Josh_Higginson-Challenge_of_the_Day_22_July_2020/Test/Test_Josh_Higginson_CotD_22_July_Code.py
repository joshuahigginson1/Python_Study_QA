"""
CotD 22nd July 2020 - TEST FILE

Task:

Define a class named Rectangle, which can be constructed by a length and width.
The Rectangle class needs to have a method that can compute area.
Finally, write a unit test to test this method.

"""

# Declare Imports ----------------------------------------------------------------------------------------------------

import pytest

from Code import Josh_Higginson_CotD_22_July_Code


# Define Tests ---------------------------------------------------------------------------------------------------

def test_expected_area():
    for tests in range(20):
        test_rect = Josh_Higginson_CotD_22_July_Code.Rectangle(4, 6)
        assert test_rect.area() == 24


def test_negative_height():
    for tests in range(20):
        test_rect = Josh_Higginson_CotD_22_July_Code.Rectangle(-4, 6)
        with pytest.raises(ValueError):
            test_rect.area()


def test_str_height():
    for tests in range(20):
        test_rect = Josh_Higginson_CotD_22_July_Code.Rectangle("Height", 6)
        with pytest.raises(ValueError):
            test_rect.area()


def test_negative_width():
    for tests in range(20):
        test_rect = Josh_Higginson_CotD_22_July_Code.Rectangle(4, -6)
        with pytest.raises(ValueError):
            test_rect.area()


def test_negative_width():
    for tests in range(20):
        test_rect = Josh_Higginson_CotD_22_July_Code.Rectangle(4, "Width")
        with pytest.raises(ValueError):
            test_rect.area()


def test_negative_height_and_width():
    for tests in range(20):
        test_rect = Josh_Higginson_CotD_22_July_Code.Rectangle(-4, -6)
        with pytest.raises(ValueError):
            test_rect.area()


def test_str_height_and_width():
    test_rect = Josh_Higginson_CotD_22_July_Code.Rectangle('Height', 'Width')
    with pytest.raises(ValueError):
        test_rect.area()
