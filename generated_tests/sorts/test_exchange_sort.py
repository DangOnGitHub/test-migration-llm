import pytest
from sorts.exchange_sort import exchange_sort

def test_exchange_sort():
    assert exchange_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert exchange_sort([-1, -2, -3]) == [-3, -2, -1]
    assert exchange_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert exchange_sort([0, 10, -2, 5, 3]) == [-2, 0, 3, 5, 10]
    assert exchange_sort([]) == []