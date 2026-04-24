import pytest
from sorts.bitonic_sort import bitonic_sort

@pytest.mark.parametrize("unsorted, expected", [
    ([12, 34, 92, -23, 0, -121, -167, 145], [-167, -121, -23, 0, 12, 34, 92, 145]),
    ([], []),
    ([5], [5]),
    ([3, 3, 3], [3, 3, 3]),
    ([5, -2], [-2, 5]),
])
def test_bitonic_sort(unsorted, expected):
    bitonic_sort(unsorted, 0, len(unsorted), 1)
    assert unsorted == expected