import pytest
from sorts.iterative_merge_sort import iter_merge_sort

def test_iter_merge_sort():
    assert iter_merge_sort([5, 9, 8, 7, 1, 2, 7]) == [1, 2, 5, 7, 7, 8, 9]
    assert iter_merge_sort([1]) == [1]
    assert iter_merge_sort([2, 1]) == [1, 2]
    assert iter_merge_sort([2, 1, 3]) == [1, 2, 3]
    assert iter_merge_sort([4, 3, 2, 1]) == [1, 2, 3, 4]
    assert iter_merge_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert iter_merge_sort(['c', 'b', 'a']) == ['a', 'b', 'c']
    assert iter_merge_sort([0.3, 0.2, 0.1]) == [0.1, 0.2, 0.3]
    assert iter_merge_sort(['dep', 'dang', 'trai']) == ['dang', 'dep', 'trai']
    assert iter_merge_sort([6]) == [6]
    assert iter_merge_sort([]) == []
    assert iter_merge_sort([-2, -9, -1, -4]) == [-9, -4, -2, -1]
    assert iter_merge_sort([1.1, 1, 0.0, -1, -1.1]) == [-1.1, -1, 0.0, 1, 1.1]
    assert iter_merge_sort('cba') == ['a', 'b', 'c']