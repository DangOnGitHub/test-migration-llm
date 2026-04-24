import pytest
from sorts.merge_insertion_sort import merge_insertion_sort

class TestMergeInsertionSort:
    def test_merge_insertion_sort(self):
        assert merge_insertion_sort([0, 5, 3, 2, 2]) == [0, 2, 2, 3, 5]
        assert merge_insertion_sort([99]) == [99]
        assert merge_insertion_sort([-2, -5, -45]) == [-45, -5, -2]
        
        from itertools import permutations
        permutations = list(permutations([0, 1, 2, 3, 4]))
        assert all(merge_insertion_sort(list(p)) == [0, 1, 2, 3, 4] for p in permutations)