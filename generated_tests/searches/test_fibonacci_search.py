import pytest
from searches.fibonacci_search import fibonacci_search

def test_fibonacci_search_found():
    array = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
    key = 128
    expected_index = 7
    assert fibonacci_search(array, key) == expected_index

def test_fibonacci_search_not_found():
    array = [1, 2, 4, 8, 16]
    key = 6
    expected_index = -1
    assert fibonacci_search(array, key) == expected_index

def test_fibonacci_search_first_element():
    array = [1, 2, 4, 8, 16]
    key = 1
    expected_index = 0
    assert fibonacci_search(array, key) == expected_index

def test_fibonacci_search_last_element():
    array = [1, 2, 4, 8, 16]
    key = 16
    expected_index = 4
    assert fibonacci_search(array, key) == expected_index

def test_fibonacci_search_single_element_found():
    array = [1]
    key = 1
    expected_index = 0
    assert fibonacci_search(array, key) == expected_index

def test_fibonacci_search_single_element_not_found():
    array = [1]
    key = 2
    expected_index = -1
    assert fibonacci_search(array, key) == expected_index

def test_fibonacci_search_empty_array():
    array = []
    key = 1
    expected_index = -1
    assert fibonacci_search(array, key) == expected_index

def test_fibonacci_search_large_array():
    array = list(range(10000))
    key = 9999
    expected_index = 9999
    assert fibonacci_search(array, key) == expected_index
