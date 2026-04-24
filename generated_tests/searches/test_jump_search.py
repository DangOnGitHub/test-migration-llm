import pytest
from searches.jump_search import jump_search

def test_jump_search_found():
    array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    key = 5
    assert jump_search(array, key) == 5, "The index of the found element should be 5."

def test_jump_search_first_element():
    array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    key = 0
    assert jump_search(array, key) == 0, "The index of the first element should be 0."

def test_jump_search_last_element():
    array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    key = 10
    assert jump_search(array, key) == 10, "The index of the last element should be 10."

def test_jump_search_not_found():
    array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    key = -1
    assert jump_search(array, key) == -1, "The element should not be found in the array."

def test_jump_search_empty_array():
    array = []
    key = 1
    assert jump_search(array, key) == -1, "The element should not be found in an empty array."

def test_jump_search_large_array():
    array = [i * 2 for i in range(1000)]
    key = 256
    assert jump_search(array, key) == 128, "The index of the found element should be 128."

def test_jump_search_large_array_not_found():
    array = [i * 2 for i in range(1000)]
    key = 999
    assert jump_search(array, key) == -1, "The element should not be found in the array."
