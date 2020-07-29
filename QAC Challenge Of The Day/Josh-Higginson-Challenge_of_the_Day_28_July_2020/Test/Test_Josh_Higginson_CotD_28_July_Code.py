"""

TEST CODE

Task: Given a string, return the number of times "am" appears in the string...
 ...BUT ONLY WHEN "am" is not followed or preceded by any other LETTERS.
"""

# Imports --------------------------------------------------------------------------------

import pytest

from Code import Josh_Higginson_CotD_28_July_Code


# Variables --------------------------------------------------------------------------------


# Tests ----------------------------------------------------------------------------------

def test_for_amsterdam():
    am = "am"
    test1 = Josh_Higginson_CotD_28_July_Code.amsterdam("Am I in Amsterdam", am)
    test2 = Josh_Higginson_CotD_28_July_Code.amsterdam("I aM in amsterdam Am I?", am)
    test3 = Josh_Higginson_CotD_28_July_Code.amsterdam("I was in Amsterdam", am)
    assert test1 == 1
    assert test2 == 2
    assert test3 == 0
