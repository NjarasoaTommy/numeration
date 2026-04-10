from outils.transform import *
def test_binary_to_decimal():
    assert binary_to_decimal(10) == 2
    assert binary_to_decimal(111) == 7
    assert binary_to_decimal(1111) == 15

def test_decimal_to_binary():
    assert decimal_to_binary(2) == 10
    assert decimal_to_binary(16) == 10000
    assert decimal_to_binary(3) == 11
    assert decimal_to_binary(7) == 111