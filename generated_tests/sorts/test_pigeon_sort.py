import pytest
from sorts.pigeon_sort import pigeon_sort

@pytest.mark.parametrize(
    "input_array, expected_array",
    [
        ([], []),
        ([4], [4]),
        ([6, 1, 99, 27, 15, 23, 36], [1, 6, 15, 23, 27, 36, 99]),
        ([6, 1, 27, 15, 23, 27, 36, 23], [1, 6, 15, 23, 23, 27, 27, 36]),
        ([5, 5, 5, 5, 5], [5, 5, 5, 5, 5]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
    ]
)
def test_pigeon_sort(input_array, expected_array):
    assert pigeon_sort(input_array) == expected_array

def test_with_negative_numbers():
    assert pigeon_sort([3, 1, 4, 1, 5, -9]) == [-9, 1, 1, 3, 4, 5]
    assert pigeon_sort([-1]) == [-1]