import pytest
from sorts.patience_sort import patience_sort

def test_patience_sort_empty():
    assert patience_sort([]) == []

def test_patience_sort_single_element():
    assert patience_sort([1]) == [1]

def test_patience_sort_sorted():
    assert patience_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_patience_sort_reverse():
    assert patience_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_patience_sort_unsorted():
    assert patience_sort([1, 9, 5, 21, 17, 6]) == [1, 5, 6, 9, 17, 21]

def test_patience_sort_negative_numbers():
    assert patience_sort([-3, -17, -48]) == [-48, -17, -3]

def test_patience_sort_mixed_numbers():
    assert patience_sort([-1, 0, 1, -2, 2]) == [-2, -1, 0, 1, 2]

def test_patience_sort_duplicates():
    assert patience_sort([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5]

def test_patience_sort_floats():
    assert patience_sort([1.2, 3.5, 2.8, 4.0, 0.5]) == [0.5, 1.2, 2.8, 3.5, 4.0]