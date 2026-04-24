import pytest
from sorts.merge_sort import merge_sort

def test_merge_sort():
    assert merge_sort([0, 5, 3, 2, 2]) == [0, 2, 2, 3, 5]
    assert merge_sort([]) == []
    assert merge_sort([-2, -5, -45]) == [-45, -5, -2]
    assert merge_sort([1]) == [1]
    assert merge_sort([3, -1, 4, 1, 5, -9, -2, 6, -5, 3, 5, -8, 9, 7]) == [-9, -8, -5, -2, -1, 1, 3, 3, 4, 5, 5, 6, 7, 9]
    assert merge_sort([1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1]