import random
from searches.linear_search import linear_search

def test_linear_search_found():
    array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    key = 5
    assert linear_search(array, key) == 5, "The index of the found element should be 5."

def test_linear_search_first_element():
    array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    key = 0
    assert linear_search(array, key) == 0, "The index of the first element should be 0."

def test_linear_search_last_element():
    array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    key = 10
    assert linear_search(array, key) == 10, "The index of the last element should be 10."

def test_linear_search_not_found():
    array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    key = -1
    assert linear_search(array, key) == -1, "The element should not be found in the array."

def test_linear_search_empty_array():
    array = []
    key = 1
    assert linear_search(array, key) == -1, "The element should not be found in an empty array."

def test_linear_search_large_array():
    array = list(range(1000))
    key = 256
    assert linear_search(array, key) == 256, "The index of the found element should be 256."

def test_linear_search_large_array_not_found():
    array = list(range(1000))
    key = 1001
    assert linear_search(array, key) == -1, "The element should not be found in the array."

def test_linear_search_multiple_occurrences():
    array = [1, 2, 3, 4, 5, 3, 6, 7, 3]
    key = 3
    assert linear_search(array, key) == 2, "The index of the first occurrence of the element should be 2."

def test_linear_search_random_array():
    array = random.sample(range(1000), 1000)
    key_index = random.randint(0, 999)
    key = array[key_index]
    assert linear_search(array, key) == key_index, "The index of the found element should match."