from outils.transform import *
def test_binary_to_decimal():
    assert binary_to_decimal(10) == 2
    assert binary_to_decimal(111) == 7
    assert binary_to_decimal(1111) == 15