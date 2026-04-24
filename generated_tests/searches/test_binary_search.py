import pytest
from searches.binary_search import binary_search, binary_search_with_duplicates

def test_binary_search_found():
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    key = 7
    expected_index = 6
    assert binary_search(array, key) == expected_index, "The index of the found element should be 6."

def test_binary_search_not_found():
    array = [1, 2, 3, 4, 5]
    key = 6
    expected_index = -1
    assert binary_search(array, key) == expected_index, "The element should not be found in the array."

def test_binary_search_first_element():
    array = [1, 2, 3, 4, 5]
    key = 1
    expected_index = 0
    assert binary_search(array, key) == expected_index, "The index of the first element should be 0."

def test_binary_search_last_element():
    array = [1, 2, 3, 4, 5]
    key = 5
    expected_index = 4
    assert binary_search(array, key) == expected_index, "The index of the last element should be 4."

def test_binary_search_single_element_found():
    array = [1]
    key = 1
    expected_index = 0
    assert binary_search(array, key) == expected_index, "The index of the single element should be 0."

def test_binary_search_single_element_not_found():
    array = [1]
    key = 2
    expected_index = -1
    assert binary_search(array, key) == expected_index, "The element should not be found in the array."

def test_binary_search_empty_array():
    array = []
    key = 1
    expected_index = -1
    assert binary_search(array, key) == expected_index, "The element should not be found in an empty array."

def test_binary_search_large_array():
    array = list(range(10000))
    key = 9999
    expected_index = 9999
    assert binary_search(array, key) == expected_index, "The index of the last element should be 9999."

def test_binary_search_null_array():
    array = []
    key = 5
    expected_index = -1
    assert binary_search(array, key) == expected_index, "The element should not be found in a null array."

def test_binary_search_with_duplicates():
    array = [1, 2, 2, 2, 3]
    key = 2

    result = binary_search(array, key)
    assert array[result] == key, "The returned index should contain the searched element."

def test_binary_search_all_elements_same():
    array = [5, 5, 5, 5, 5]
    key = 5

    result = binary_search(array, key)
    assert array[result] == key, "The returned index should contain the searched element."

def test_binary_search_negative_numbers():
    array = [-10, -5, 0, 5, 10]
    key = -5
    expected_index = 1
    assert binary_search(array, key) == expected_index, "The index of the element should be 1."

def test_binary_search_key_smaller_than_all():
    array = [10, 20, 30]
    key = 5
    expected_index = -1
    assert binary_search(array, key) == expected_index, "The element should not be found in the array."

def test_binary_search_key_larger_than_all():
    array = [10, 20, 30]
    key = 40
    expected_index = -1
    assert binary_search(array, key) == expected_index, "The element should not be found in the array."

def test_binary_search_strings():
    array = ["apple", "banana", "cherry", "date"]
    key = "cherry"
    expected_index = 2
    assert binary_search(array, key) == expected_index, "The index of the element should be 2."