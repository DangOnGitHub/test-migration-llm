import pytest
from sorts.wiggle_sort import wiggle_sort

@pytest.mark.parametrize("values, result", [
    ([1, 2, 3, 4], [1, 4, 2, 3]),
    ([1, 2, 3, 4, 5], [3, 5, 1, 4, 2]),
    ([7, 2, 2, 2, 5], [2, 7, 2, 5, 2]),
    ([1, 1, 2, 2, 5], [2, 5, 1, 2, 1]),
    ([1, 1, 2, 2, 2, 5], [2, 5, 1, 2, 1, 2]),
    ([1, 2, 4, 4], [1, 4, 2, 4]),
    (["a", "b", "d", "c"], ["a", "d", "b", "c"])
])
def test_wiggle_sort(values, result):
    assert wiggle_sort(values) == result