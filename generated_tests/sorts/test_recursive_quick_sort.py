import pytest
from sorts.recursive_quick_sort import quick_sort

def test_quick_sort():
    assert quick_sort([2, 1, 0]) == [0, 1, 2]
    assert quick_sort([5, 3, 8, 4, 2]) == [2, 3, 4, 5, 8]
    assert quick_sort([5]) == [5]
    assert quick_sort([]) == []
    assert quick_sort(['b', 'a', 'c']) == ['a', 'b', 'c']
    assert quick_sort([2.2, 3.3, 1.1, 5.5]) == [1.1, 2.2, 3.3, 5.5]
    assert quick_sort("quick_sort") == sorted("quick_sort")

pytest.main()