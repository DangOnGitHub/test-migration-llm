import pytest
from dynamic_programming.sum_of_subset import is_sum_subset

def test_basic_check():
    assert is_sum_subset([1, 2, 7, 10, 9], 14) is False
    assert is_sum_subset([2, 15, 1, 6, 7], 4) is False
    assert is_sum_subset([7, 3, 2, 5, 8], 14) is True
    assert is_sum_subset([4, 3, 2, 1], 5) is True
    assert is_sum_subset([1, 7, 2, 9, 10], 13) is True