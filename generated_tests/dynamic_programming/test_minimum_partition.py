import pytest
from dynamic_programming.minimum_partition import find_min

def test_find_min_with_even_sum():
    array = [1, 6, 11, 4]
    assert find_min(array) == 0

def test_find_min_with_odd_sum():
    array = [36, 7, 46, 40]
    assert find_min(array) == 23

def test_find_min_with_single_element():
    array = [7]
    assert find_min(array) == 7

def test_find_min_with_large_numbers():
    array = [100, 200, 300, 400, 500]
    assert find_min(array) == 100

def test_find_min_with_empty_array():
    array = []
    assert find_min(array) == 0

def test_find_min_throws_for_negative_array():
    with pytest.raises(IndexError):
        find_min([4, 1, -6, 7])