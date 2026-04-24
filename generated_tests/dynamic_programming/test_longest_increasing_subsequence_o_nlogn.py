import pytest
from dynamic_programming.longest_increasing_subsequence_o_nlogn import longest_increasing_subsequence_length

@pytest.mark.parametrize("input_data, expected", [
    ([10, 9, 2, 5, 3, 7, 101, 18], 4),
    ([0, 1, 0, 3, 2, 3], 4),
    ([7, 7, 7, 7, 7], 1),
    ([1, 3, 5, 4, 7], 4),
    ([], 0),
    ([10], 1),
    ([3, 10, 2, 1, 20], 3),
    ([50, 3, 10, 7, 40, 80], 4),
])
def test_longest_increasing_subsequence_length(input_data, expected):
    assert longest_increasing_subsequence_length(input_data) == expected