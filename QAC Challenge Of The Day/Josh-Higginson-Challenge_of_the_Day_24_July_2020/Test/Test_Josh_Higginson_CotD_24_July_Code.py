"""

TEST CODE

Task:

Write a function that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program: 9 Then, the output should be: 11106 (i.e. 9+99+999+9999)


"""

# Imports --------------------------------------------------------------------------------

import pytest

from Code import Josh_Higginson_CotD_24_July_Code

# Tests ----------------------------------------------------------------------------------

def test_for_num():
    assert Josh_Higginson_CotD_July_Code.cotd_24_july(0) == 0
    assert Josh_Higginson_CotD_July_Code.cotd_24_july(1) == 1234
    assert Josh_Higginson_CotD_July_Code.cotd_24_july(2) == 2468
    assert Josh_Higginson_CotD_July_Code.cotd_24_july(3) == 3702
    assert Josh_Higginson_CotD_July_Code.cotd_24_july(4) == 4936
    assert Josh_Higginson_CotD_July_Code.cotd_24_july(5) == 6170
    assert Josh_Higginson_CotD_July_Code.cotd_24_july(6) == 7404
    assert Josh_Higginson_CotD_July_Code.cotd_24_july(7) == 8638
    assert Josh_Higginson_CotD_July_Code.cotd_24_july(8) == 9872
    assert Josh_Higginson_CotD_July_Code.cotd_24_july(9) == 11106
    assert Josh_Higginson_CotD_July_Code.cotd_24_july(10) == 10203040
