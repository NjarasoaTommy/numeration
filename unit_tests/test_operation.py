from outils.operation import *
from outils.transform import *
def test_split_number():
    assert split_number(12345) == [1, 2, 3, 4, 5]
    assert split_number(2904) == [2, 9, 0, 4]
    assert split_number(117904) == [1, 1, 7, 9, 0, 4]

def test_element_addition():
    assert element_addition(0, 0) == (0, 0)
    assert element_addition(1, 1) == (1, 0)
    assert element_addition(1, 0) == (0, 1)
    assert element_addition(0, 1) == (0, 1)

def test_join_number():
    assert join_number([1, 2, 4, 5, 6]) == 12456
    assert join_number([1, 0, 4, 0, 6]) == 10406
    assert join_number([9, 8, 2, 0, 0]) == 98200
    assert join_number([5, 4, 2, 0, 0, 1, 7]) == 5420017
    assert join_number([5, 4, 2, 0, 0, 1, 7]) == 5420017
    assert join_number([5, 0, 0, 0, 0, 9, 3]) == 5000093

def test_addition():
    assert addition(decimal_to_binary(3), decimal_to_binary(1)) == decimal_to_binary(3 + 1)
    assert addition(decimal_to_binary(12), decimal_to_binary(5)) == decimal_to_binary(12 + 5)
    assert addition(100, 10) == 110
    assert addition(100, 1) == 101
    assert addition(11, 11) == 110
    assert addition(decimal_to_binary(45), decimal_to_binary(5)) == decimal_to_binary(45 + 5)
    assert addition(decimal_to_binary(133), decimal_to_binary(300)) == decimal_to_binary(133 + 300)