import pytest
from sorts.intro_sort import sort

class TestIntrospectiveSort:
    def test_sort_integers(self):
        assert sort([4, 2, 6, 8, 1, 7, 8, 22, 14, 56, 27, 79, 23, 45, 14, 12]) == [1, 2, 4, 6, 7, 8, 8, 12, 14, 14, 22, 23, 27, 45, 56, 79]
        assert sort([-1, -5, -3, -13, -44]) == [-44, -13, -5, -3, -1]
        assert sort([]) == []
        assert sort([5]) == [5]
        assert sort([-3, 0, -7, 6, 23, -34]) == [-34, -7, -3, 0, 6, 23]

    def test_sort_floats(self):
        assert sort([1.7, 1.0, 3.3, 2.1, 0.3]) == [0.3, 1.0, 1.7, 2.1, 3.3]

    def test_sort_strings(self):
        assert sort(['d', 'a', 'b', 'e', 'c']) == ['a', 'b', 'c', 'd', 'e']