import pytest
from searches.interpolation_search import interpolation_search


def test_interpolation_search_found():
    sorted_collection = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
    key = 128
    expected_index = 7
    assert interpolation_search(sorted_collection, key) == expected_index, "The index of the found element should be 7."


def test_interpolation_search_not_found():
    sorted_collection = [1, 2, 4, 8, 16]
    key = 6
    assert interpolation_search(sorted_collection, key) is None, "The element should not be found in the array."


def test_interpolation_search_first_element():
    sorted_collection = [1, 2, 4, 8, 16]
    key = 1
    assert interpolation_search(sorted_collection, key) == 0, "The index of the first element should be 0."


def test_interpolation_search_single_element_not_found():
    sorted_collection = [1]
    key = 2
    assert interpolation_search(sorted_collection, key) is None, "The element should not be found in the array."


def test_interpolation_search_empty_array():
    sorted_collection = []
    key = 1
    assert interpolation_search(sorted_collection, key) is None, "The element should not be found in an empty array."


def test_interpolation_search_large_uniform_array():
    sorted_collection = list(range(0, 10000, 2))
    key = 9998
    assert interpolation_search(sorted_collection, key) == 4999, "The index of the last element should be 4999."


def test_interpolation_search_large_non_uniform_array():
    sorted_collection = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]  # Fibonacci numbers
    key = 21
    assert interpolation_search(sorted_collection, key) == 6, "The index of the found element should be 6."