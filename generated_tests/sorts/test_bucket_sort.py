import pytest
from sorts.bucket_sort import bucket_sort

def test_bucket_sort():
    assert bucket_sort([-1, 2, -5, 0]) == sorted([-1, 2, -5, 0])
    assert bucket_sort([9, 8, 7, 6, -12]) == sorted([9, 8, 7, 6, -12])
    assert bucket_sort([.4, 1.2, .1, .2, -.9]) == sorted([.4, 1.2, .1, .2, -.9])
    assert bucket_sort([]) == sorted([])
    assert bucket_sort([-1e10, 1e10]) == sorted([-1e10, 1e10])
    import random
    collection = random.sample(range(-50, 50), 50)
    assert bucket_sort(collection) == sorted(collection)
    assert bucket_sort([1, 2, 2, 1, 1, 3]) == sorted([1, 2, 2, 1, 1, 3])
    assert bucket_sort([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5]
    assert bucket_sort([1000, -1000, 500, -500, 0]) == sorted([1000, -1000, 500, -500, 0])
    assert bucket_sort([5.5, 2.2, -1.1, 3.3, 0.0]) == sorted([5.5, 2.2, -1.1, 3.3, 0.0])
    assert bucket_sort([1]) == [1]
    assert bucket_sort([-1.1, -1.5, -3.4, 2.5, 3.6, -3.3]) == sorted([-1.1, -1.5, -3.4, 2.5, 3.6, -3.3])
    assert bucket_sort([9, 2, 7, 1, 5]) == sorted([9, 2, 7, 1, 5])
    assert bucket_sort([4, 5, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert bucket_sort([0, 1, -10, 15, 2, -2]) == [-10, -2, 0, 1, 2, 15]
    assert bucket_sort([1.1, 1.2, -1.2, 0, 2.4]) == [-1.2, 0, 1.1, 1.2, 2.4]
    assert bucket_sort([-5, -1, -6, -2]) == [-6, -5, -2, -1]