import pytest
from sorts.comb_sort import comb_sort

@pytest.mark.parametrize("data, expected", [
    ([0, 5, 3, 2, 2], [0, 2, 2, 3, 5]),
    ([], []),
    ([99, 45, -7, 8, 2, 0, -15, 3], [-15, -7, 0, 2, 3, 8, 45, 99]),
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([2, 3, 5, 3, 2, 1], [1, 2, 2, 3, 3, 5]),
])
def test_comb_sort(data, expected):
    assert comb_sort(data) == expected