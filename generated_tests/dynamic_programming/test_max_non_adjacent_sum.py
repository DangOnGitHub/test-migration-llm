import pytest
from dynamic_programming.max_non_adjacent_sum import maximum_non_adjacent_sum

def test_maximum_non_adjacent_sum_with_empty_array():
    assert maximum_non_adjacent_sum([]) == 0  # Empty array

def test_maximum_non_adjacent_sum_with_single_element():
    assert maximum_non_adjacent_sum([1]) == 1  # Single element

def test_maximum_non_adjacent_sum_with_two_elements_take_max():
    assert maximum_non_adjacent_sum([1, 2]) == 2  # Take max of both

def test_maximum_non_adjacent_sum_with_multiple_elements():
    assert maximum_non_adjacent_sum([3, 2, 5, 10, 7]) == 15  # 3 + 7 + 5
    assert maximum_non_adjacent_sum([5, 1, 1, 5]) == 10  # 5 + 5

if __name__ == "__main__":
    pytest.main()