from sorts.strand_sort import strand_sort

def test_strand_sort():
    assert strand_sort([4, 3, 5, 1, 2]) == [1, 2, 3, 4, 5]
    assert strand_sort([4, 3, 5, 1, 2], reverse=True) == [5, 4, 3, 2, 1]
    assert strand_sort([]) == []
    assert strand_sort([5]) == [5]
    assert strand_sort([3, 1, 4, 1, 5, 9, 2, 6]) == [1, 1, 2, 3, 4, 5, 6, 9]
    assert strand_sort([3, 1, 4, 1, 5, 9, 2, 6], reverse=True) == [9, 6, 5, 4, 3, 2, 1, 1]