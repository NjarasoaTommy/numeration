from outils.operation import *
def test_split_number():
    assert split_number(12345) == [1, 2, 3, 4, 5]
    assert split_number(2904) == [2, 9, 0, 4]
    assert split_number(117904) == [1, 1, 7, 9, 0, 4]