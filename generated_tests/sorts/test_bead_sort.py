import pytest
from sorts.bead_sort import bead_sort

@pytest.mark.parametrize("input_array, expected_array", [
    ([], []),
    ([4], [4]),
    ([6, 1, 99, 27, 15, 23, 36], [1, 6, 15, 23, 27, 36, 99]),
    ([6, 1, 27, 15, 23, 27, 36, 23], [1, 6, 15, 23, 23, 27, 27, 36]),
    ([5, 5, 5, 5, 5], [5, 5, 5, 5, 5]),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5])
])
def test_bead_sort(input_array, expected_array):
    assert bead_sort(input_array) == expected_array

def test_with_negative_numbers():
    with pytest.raises(TypeError, match="Sequence must be list of non-negative integers"):
        bead_sort([3, 1, 4, 1, 5, -9])