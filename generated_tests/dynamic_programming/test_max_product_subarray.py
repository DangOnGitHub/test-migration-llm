import pytest
from dynamic_programming.max_product_subarray import max_product_subarray

def test_all_positive_numbers():
    nums = [2, 3, 4]
    expected = 24
    actual = max_product_subarray(nums)
    assert expected == actual, "The maximum product should be 24."

def test_mixed_positive_and_negative():
    nums = [2, -3, -4, 1]
    expected = 24
    actual = max_product_subarray(nums)
    assert expected == actual, "The maximum product should be 24."

def test_array_with_zeros():
    nums = [2, 3, 0, 4, 6]
    expected = 24
    actual = max_product_subarray(nums)
    assert expected == actual, "The maximum product should be 24."

def test_single_element():
    nums = [5]
    expected = 5
    actual = max_product_subarray(nums)
    assert expected == actual, "The maximum product should be 5."

def test_all_negative_numbers():
    nums = [-2, -3, -4]
    expected = 12
    actual = max_product_subarray(nums)
    assert expected == actual, "The maximum product should be 12."

def test_odd_negative_numbers():
    nums = [-2, -3, 10, -1]
    expected = 60
    actual = max_product_subarray(nums)
    assert expected == actual, "The maximum product should be 60."

def test_empty_array():
    nums = []
    expected = 0
    actual = max_product_subarray(nums)
    assert expected == actual, "The maximum product should be 0 for an empty array."

def test_none_array():
    nums = None
    expected = 0
    actual = max_product_subarray(nums)
    assert expected == actual, "The maximum product should be 0 for a None input."

def test_alternating_numbers():
    nums = [2, 3, -2, 4]
    expected = 6
    actual = max_product_subarray(nums)
    assert expected == actual, "The maximum product should be 6."

def test_large_numbers():
    nums = [6, -3, -20, 0, 5]
    expected = 360
    actual = max_product_subarray(nums)
    assert expected == actual, "The maximum product should be 360."

def test_single_negative_element():
    nums = [-8]
    expected = -8
    actual = max_product_subarray(nums)
    assert expected == actual, "The maximum product should be -8."

def test_multiple_zeros():
    nums = [0, 2, 3, 0, 4]
    expected = 6
    actual = max_product_subarray(nums)
    assert expected == actual, "The maximum product should be 6."