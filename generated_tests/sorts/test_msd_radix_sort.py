import pytest
from sorts.msd_radix_sort import msd_radix_sort, msd_radix_sort_inplace

@pytest.mark.parametrize("input_array, expected_array", [
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
    ([123, 9, 54321, 123456789, 0], [0, 9, 123, 54321, 123456789])
])
def test_msd_radix_sort(input_array, expected_array):
    assert msd_radix_sort(input_array) == expected_array

def test_msd_radix_sort_with_negative_numbers():
    with pytest.raises(ValueError, match="All numbers must be positive"):
        msd_radix_sort([3, 1, 4, 1, 5, -9])

@pytest.mark.parametrize("input_array, expected_array", [
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
    ([123, 9, 54321, 123456789, 0], [0, 9, 123, 54321, 123456789])
])
def test_msd_radix_sort_inplace(input_array, expected_array):
    msd_radix_sort_inplace(input_array)
    assert input_array == expected_array

def test_msd_radix_sort_inplace_with_negative_numbers():
    with pytest.raises(ValueError, match="All numbers must be positive"):
        msd_radix_sort_inplace([3, 1, 4, 1, 5, -9])