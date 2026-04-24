import pytest
from sorts.unknown_sort import merge_sort

def test_merge_sort():
    assert merge_sort([0, 5, 3, 2, 2]) == [0, 2, 2, 3, 5]
    assert merge_sort([]) == []
    assert merge_sort([-2, -5, -45]) == [-45, -5, -2]
    assert merge_sort([1]) == [1]
    assert merge_sort([2, 1]) == [1, 2]
    assert merge_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert merge_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert merge_sort([3, 1, 4, 2, 5]) == [1, 2, 3, 4, 5]