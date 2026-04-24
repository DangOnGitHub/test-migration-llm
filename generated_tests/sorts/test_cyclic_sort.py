import pytest
from sorts.cyclic_sort import cyclic_sort

@pytest.mark.parametrize("unsorted, sorted_array", [
    ([], []),
    ([3, 5, 2, 1, 4], [1, 2, 3, 4, 5]),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
    ([2, 3, 1], [1, 2, 3]),
    ([1], [1]),
    ([1, 6, 2, 5, 3], [1, 2, 3, 5, 6]),  # Example having missing and extra integer
])
def test_cyclic_sort(unsorted, sorted_array):
    assert cyclic_sort(unsorted) == sorted_array