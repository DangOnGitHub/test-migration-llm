import pytest
from sorts.quick_sort import quick_sort

def test_quick_sort():
    # Test empty list
    assert quick_sort([]) == []
    
    # Test already sorted list
    assert quick_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    # Test reverse sorted list
    assert quick_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

    # Test list with negative numbers
    assert quick_sort([-2, 5, 0, -45]) == [-45, -2, 0, 5]

    # Test list with duplicate numbers
    assert quick_sort([0, 5, 3, 2, 2]) == [0, 2, 2, 3, 5]

    # Test list with single element
    assert quick_sort([1]) == [1]

    # Test list with all same elements
    assert quick_sort([2, 2, 2, 2]) == [2, 2, 2, 2]