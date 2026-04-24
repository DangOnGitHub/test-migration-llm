import pytest
from sorts.selection_sort import selection_sort

def test_selection_sort():
    assert selection_sort([0, 5, 3, 2, 2]) == [0, 2, 2, 3, 5]
    assert selection_sort([]) == []
    assert selection_sort([-2, -5, -45]) == [-45, -5, -2]
    assert selection_sort([12, 4, 5, 3, 8, 7]) == [3, 4, 5, 7, 8, 12]
    assert selection_sort([1]) == [1]
    assert selection_sort([2, 1]) == [1, 2]
    # Test with repeated elements
    assert selection_sort([2, 3, 2, 3, 1]) == [1, 2, 2, 3, 3]
    # Test with already sorted list
    assert selection_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    # Test with reverse sorted list
    assert selection_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]