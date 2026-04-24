import pytest
from sorts.heap_sort import heap_sort

@pytest.mark.parametrize("unsorted, expected", [
    ([0, 5, 3, 2, 2], [0, 2, 2, 3, 5]),
    ([], []),
    ([-2, -5, -45], [-45, -5, -2]),
    ([3, 7, 9, 28, 123, -5, 8, -30, -200, 0, 4], [-200, -30, -5, 0, 3, 4, 7, 8, 9, 28, 123]),
    ([1, 4, 3, 5, 2], [1, 2, 3, 4, 5])
])
def test_heap_sort(unsorted, expected):
    assert heap_sort(unsorted) == expected