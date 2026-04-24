import pytest
from maths.perfect_square import perfect_square, perfect_square_binary_search

@pytest.mark.parametrize("number", [0, 1, 2 * 2, 3 * 3, 4 * 4, 5 * 5, 6 * 6, 7 * 7, 8 * 8, 9 * 9, 10 * 10, 11 * 11, 123 * 123])
def test_positive_cases(number):
    assert perfect_square(number)
    assert perfect_square_binary_search(number)

@pytest.mark.parametrize("number", [-1, -2, -3, -4, -5, -100, 2, 3, 5, 6, 7, 8, 10, 11, 12, 13, 15, 17, 99, 101, 257, 999, 1001])
def test_negative_cases(number):
    assert not perfect_square(number)
    assert not perfect_square_binary_search(number)