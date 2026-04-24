import pytest
from sorts.shrink_shell_sort import shell_sort

@pytest.mark.parametrize("unsorted_collection, sorted_collection", [
    ([3, 2, 1], [1, 2, 3]),
    ([], []),
    ([1], [1]),
    (['banana', 'apple', 'cherry'], ['apple', 'banana', 'cherry']),
    ([5, -1, 0, 3, 2], [-1, 0, 2, 3, 5]),
    ([9, 8, 7, 6, 5, 4, 3, 2, 1, 0], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
    ([4, 5, 6, 3, 2, 1], [1, 2, 3, 4, 5, 6])
])
def test_shell_sort(unsorted_collection, sorted_collection):
    assert shell_sort(unsorted_collection) == sorted_collection