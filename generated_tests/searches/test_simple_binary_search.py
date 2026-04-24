import pytest
from searches.simple_binary_search import binary_search

def test_binary_search_found():
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    key = 7
    assert binary_search(array, key)

def test_binary_search_not_found():
    array = [1, 2, 3, 4, 5]
    key = 6
    assert not binary_search(array, key)

def test_binary_search_first_element():
    array = [1, 2, 3, 4, 5]
    key = 1
    assert binary_search(array, key)

def test_binary_search_last_element():
    array = [1, 2, 3, 4, 5]
    key = 5
    assert binary_search(array, key)

def test_binary_search_single_element_found():
    array = [1]
    key = 1
    assert binary_search(array, key)

def test_binary_search_single_element_not_found():
    array = [1]
    key = 2
    assert not binary_search(array, key)

def test_binary_search_empty_array():
    array = []
    key = 1
    assert not binary_search(array, key)

def test_binary_search_large_array():
    array = list(range(10000))
    key = 9999
    assert binary_search(array, key)

def test_binary_search_with_duplicates():
    array = [1, 2, 2, 2, 3]
    key = 2
    assert binary_search(array, key)

def test_binary_search_all_elements_same():
    array = [5, 5, 5, 5, 5]
    key = 5
    assert binary_search(array, key)

def test_binary_search_negative_numbers():
    array = [-10, -5, 0, 5, 10]
    key = -5
    assert binary_search(array, key)

def test_binary_search_key_smaller_than_all():
    array = [10, 20, 30]
    key = 5
    assert not binary_search(array, key)

def test_binary_search_key_larger_than_all():
    array = [10, 20, 30]
    key = 40
    assert not binary_search(array, key)

def test_binary_search_strings():
    array = ["apple", "banana", "cherry", "date"]
    key = "cherry"
    assert binary_search(array, key)