import pytest
from searches.sentinel_linear_search import sentinel_linear_search

def test_sentinel_linear_search_found():
    array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    key = 5
    assert sentinel_linear_search(array, key) == 5, "The index of the found element should be 5."

def test_sentinel_linear_search_first_element():
    array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    key = 0
    assert sentinel_linear_search(array, key) == 0, "The index of the first element should be 0."

def test_sentinel_linear_search_last_element():
    array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    key = 10
    assert sentinel_linear_search(array, key) == 9, "The index of the last element should be 9."

def test_sentinel_linear_search_not_found():
    array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    key = -1
    assert sentinel_linear_search(array, key) is None, "The element should not be found in the array."

def test_sentinel_linear_search_empty_array():
    array = []
    key = 1
    assert sentinel_linear_search(array, key) is None, "The element should not be found in an empty array."

def test_sentinel_linear_search_single_element_found():
    array = [42]
    key = 42
    assert sentinel_linear_search(array, key) == 0, "The element should be found at index 0."

def test_sentinel_linear_search_single_element_not_found():
    array = [42]
    key = 24
    assert sentinel_linear_search(array, key) is None, "The element should not be found in the array."

def test_sentinel_linear_search_multiple_occurrences():
    array = [1, 2, 3, 4, 5, 3, 6, 7, 3]
    key = 3
    assert sentinel_linear_search(array, key) == 2, "The index of the first occurrence of the element should be 2."

def test_sentinel_linear_search_large_array():
    array = list(range(1000))
    key = 256
    assert sentinel_linear_search(array, key) == 256, "The index of the found element should be 256."

def test_sentinel_linear_search_large_array_not_found():
    array = list(range(1000))
    key = 1001
    assert sentinel_linear_search(array, key) is None, "The element should not be found in the array."

def test_sentinel_linear_search_null_key():
    array = [1, None, 3, 4, None]
    key = None
    assert sentinel_linear_search(array, key) == 1, "The index of the first null element should be 1."

def test_sentinel_linear_search_null_key_not_found():
    array = [1, 2, 3, 4, 5]
    key = None
    assert sentinel_linear_search(array, key) is None, "Null key should not be found in array without null elements."

def test_sentinel_linear_search_string_array():
    array = ["apple", "banana", "cherry", "date", "elderberry"]
    key = "cherry"
    assert sentinel_linear_search(array, key) == 2, "The index of 'cherry' should be 2."

def test_sentinel_linear_search_string_array_not_found():
    array = ["apple", "banana", "cherry", "date", "elderberry"]
    key = "grape"
    assert sentinel_linear_search(array, key) is None, "The element 'grape' should not be found in the array."

def test_sentinel_linear_search_array_integrity():
    array = [1, 2, 3, 4, 5]
    original_array = array.copy()
    key = 3
    sentinel_linear_search(array, key)
    assert array == original_array, "Array should remain unchanged after search."

def test_sentinel_linear_search_key_equals_last_element():
    array = [1, 2, 3, 4, 5, 3]
    key = 3
    assert sentinel_linear_search(array, key) == 2, "Should find the first occurrence at index 2, not the last."