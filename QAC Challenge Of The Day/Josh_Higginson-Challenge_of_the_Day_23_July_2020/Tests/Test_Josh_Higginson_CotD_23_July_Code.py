"""
TEST FILE

Task: Write a function that accepts a seq of whitespace separated words as a string input, sorts
each item alphanumerically and removes any duplicate items.

Return the result as a string.

Dev Notes:


"""

# Imports --------------------------------------------------------------------------------

import pytest
from Code import Josh_Higginson_CotD_23_July_Code

# Variables ------------------------------------------------------------------------------

number_of_repeats = 1


# Tests ----------------------------------------------------------------------------------

def test_for_lower():
    for repeats in range(number_of_repeats):
        assert Josh_Higginson_CotD_23_July_Code.word_sorter(
            "woodworm apple coffee simple shiny shellshock aardvark") == "aardvark apple coffee shellshock shiny simple woodworm"


def test_for_mults():
    for repeats in range(number_of_repeats):
        assert Josh_Higginson_CotD_23_July_Code.word_sorter(
            "ant ant ant ant Ant Ant Ant Ant Anteater") == "Ant ant Anteater"


def test_for_upper():
    for repeats in range(number_of_repeats):
        assert Josh_Higginson_CotD_23_July_Code.word_sorter(
            "Woodworm Apple coffee Simple shiny sHellshock Aardvark") == "Aardvark Apple coffee sHellshock shiny Simple Woodworm"


def test_for_num_strings():
    for repeats in range(number_of_repeats):
        assert Josh_Higginson_CotD_23_July_Code.word_sorter(
            "9oodworm 9pple 3offee 6imple 8hiny 56hellshock 3ardvark") == "3ardvark 3offee 56hellshock 6imple 8hiny 9oodworm 9pple"


def test_for_num_ints():
    for repeats in range(number_of_repeats):
        assert Josh_Higginson_CotD_23_July_Code.word_sorter(1, 2, 3, 4, 5) == "1 2 3 4 5"
