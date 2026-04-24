import pytest
from searches.exponential_search import exponential_search

def test_exponential_search_found():
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    key = 7
    expected_index = 6  # Index of the key in the array
    assert exponential_search(array, key) == expected_index

def test_exponential_search_first_element():
    array = [1, 2, 3, 4, 5]
    key = 1  # First element
    expected_index = 0  # Index of the key in the array
    assert exponential_search(array, key) == expected_index

def test_exponential_search_last_element():
    array = [1, 2, 3, 4, 5]
    key = 5  # Last element
    expected_index = 4  # Index of the key in the array
    assert exponential_search(array, key) == expected_index

def test_exponential_search_single_element_found():
    array = [1]
    key = 1  # Only element present
    expected_index = 0  # Index of the key in the array
    assert exponential_search(array, key) == expected_index

def test_exponential_search_empty_array():
    array = []  # Empty array
    key = 1  # Key not present
    expected_index = -1  # Key not found
    assert exponential_search(array, key) == expected_index

def test_exponential_search_large_array():
    array = list(range(10000))  # Array from 0 to 9999
    key = 9999
    expected_index = 9999
    assert exponential_search(array, key) == expected_index