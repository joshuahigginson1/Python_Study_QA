# Declare inputs ----------------------------------------------------------------------------------------------------

import pytest
from programs import vowels


# Declare Tests -----------------------------------------------------------------------------------------------------

def test_vowels_upper():
    assert vowels.vowels("AEIOU") == 5


def test_vowels_lower():
    assert vowels.vowels("aeiou") == 5
