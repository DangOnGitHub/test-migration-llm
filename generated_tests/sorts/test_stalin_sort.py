import pytest
from sorts.stalin_sort import stalin_sort

def test_sort_integers():
    input_data = [4, 23, 6, 78, 1, 54, 231, 9, 12]
    expected = [4, 23, 78, 231]
    assert stalin_sort(input_data) == expected

def test_sort_strings():
    input_data = ["c", "a", "e", "b", "d"]
    expected = ["c", "e"]
    assert stalin_sort(input_data) == expected

def test_sort_with_duplicates():
    input_data = [1, 3, 2, 2, 5, 4]
    expected = [1, 3, 5]
    assert stalin_sort(input_data) == expected

def test_sort_empty_array():
    input_data = []
    expected = []
    assert stalin_sort(input_data) == expected

def test_sort_single_element():
    input_data = [42]
    expected = [42]
    assert stalin_sort(input_data) == expected