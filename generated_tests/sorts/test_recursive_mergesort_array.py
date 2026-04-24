import pytest
from sorts.recursive_mergesort_array import merge

def test_merge_case1():
    assert merge([5, 12, 9, 3, 15, 88]) == [3, 5, 9, 12, 15, 88]

def test_merge_case2():
    assert merge([-3, 5, 3, 4, 3, 7, 40, -20, 30, 0]) == [-20, -3, 0, 3, 3, 4, 5, 7, 30, 40]

if __name__ == "__main__":
    pytest.main()