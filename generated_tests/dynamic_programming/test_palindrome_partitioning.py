import pytest
from dynamic_programming.palindrome_partitioning import find_minimum_partitions

@pytest.mark.parametrize("input, expected", [
    ("a", 0),
    ("aa", 0),
    ("ab", 1),
    ("ababbbabbababa", 3),
    ("abcde", 4),
    ("abacdcaba", 0),
])
def test_find_minimum_partitions(input, expected):
    assert find_minimum_partitions(input) == expected