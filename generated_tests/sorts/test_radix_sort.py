import pytest
from sorts.radix_sort import radix_sort

@pytest.mark.parametrize("input_list, expected_list", [
    ([170, 45, 75, 90, 802, 24, 2, 66], [2, 24, 45, 66, 75, 90, 170, 802]),
    ([3, 3, 3, 3], [3, 3, 3, 3]),
    ([9, 4, 6, 8, 14, 3], [3, 4, 6, 8, 9, 14]),
    ([10, 90, 49, 2, 1, 5, 23], [1, 2, 5, 10, 23, 49, 90]),
    ([1, 3, 4, 2, 7, 8], [1, 2, 3, 4, 7, 8]),
    ([], []),
    ([1], [1]),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]),
    ([9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9]),
    ([1000000000, 999999999, 888888888, 777777777], [777777777, 888888888, 999999999, 1000000000]),
    ([123, 9, 54321, 123456789, 0], [0, 9, 123, 54321, 123456789]),
])
def test_radix_sort(input_list, expected_list):
    assert radix_sort(input_list) == expected_list

def test_radix_sort_negative_numbers():
    with pytest.raises(ValueError):
        radix_sort([3, 1, 4, 1, 5, -9])