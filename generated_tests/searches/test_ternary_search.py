import pytest
from searches.ternary_search import ite_ternary_search, rec_ternary_search

def test_find_element_in_sorted_array():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 5

    result_iter = ite_ternary_search(arr, target)
    result_rec = rec_ternary_search(0, len(arr) - 1, arr, target)

    assert result_iter == 4, "Should find the element 5 at index 4"
    assert result_rec == 4, "Should find the element 5 at index 4"

def test_element_not_found():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 11

    result_iter = ite_ternary_search(arr, target)
    result_rec = rec_ternary_search(0, len(arr) - 1, arr, target)

    assert result_iter == -1, "Should return -1 for element 11 which is not present"
    assert result_rec == -1, "Should return -1 for element 11 which is not present"

def test_find_first_element():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 1

    result_iter = ite_ternary_search(arr, target)
    result_rec = rec_ternary_search(0, len(arr) - 1, arr, target)

    assert result_iter == 0, "Should find the first element 1 at index 0"
    assert result_rec == 0, "Should find the first element 1 at index 0"

def test_find_last_element():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 10

    result_iter = ite_ternary_search(arr, target)
    result_rec = rec_ternary_search(0, len(arr) - 1, arr, target)

    assert result_iter == 9, "Should find the last element 10 at index 9"
    assert result_rec == 9, "Should find the last element 10 at index 9"

def test_find_in_large_array():
    arr = list(range(1, 1001))
    target = 500

    result_iter = ite_ternary_search(arr, target)
    result_rec = rec_ternary_search(0, len(arr) - 1, arr, target)

    assert result_iter == 499, "Should find element 500 at index 499"
    assert result_rec == 499, "Should find element 500 at index 499"

def test_negative_numbers():
    arr = [-10, -5, -3, -1, 0, 1, 3, 5, 7, 10]
    target = -3

    result_iter = ite_ternary_search(arr, target)
    result_rec = rec_ternary_search(0, len(arr) - 1, arr, target)

    assert result_iter == 2, "Should find the element -3 at index 2"
    assert result_rec == 2, "Should find the element -3 at index 2"

def test_edge_case_empty_array():
    arr = []
    target = 5

    result_iter = ite_ternary_search(arr, target)
    result_rec = rec_ternary_search(0, len(arr) - 1, arr, target)

    assert result_iter == -1, "Should return -1 for an empty array"
    assert result_rec == -1, "Should return -1 for an empty array"