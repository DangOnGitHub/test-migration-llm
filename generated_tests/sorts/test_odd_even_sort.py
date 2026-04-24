import pytest
from sorts.odd_even_sort import odd_even_sort


@pytest.fixture
def sample_data():
    return [
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([], []),
        ([-10, -1, 10, 2], [-10, -1, 2, 10]),
        ([1, 2, 3, 4], [1, 2, 3, 4]),
    ]


def test_odd_even_sort(sample_data):
    for unsorted_list, expected in sample_data:
        assert odd_even_sort(unsorted_list) == expected