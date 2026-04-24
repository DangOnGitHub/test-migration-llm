import pytest
from sorts.binary_insertion_sort import binary_insertion_sort

def test_binary_insertion_sort():
    assert binary_insertion_sort([0, 4, 1234, 4, 1]) == [0, 1, 4, 4, 1234]
    assert binary_insertion_sort([]) == sorted([])
    assert binary_insertion_sort([-1, -2, -3]) == sorted([-1, -2, -3])
    
    lst = ['d', 'a', 'b', 'e', 'c']
    assert binary_insertion_sort(lst) == sorted(lst)
    
    import random
    collection = random.sample(range(-50, 50), 100)
    assert binary_insertion_sort(collection) == sorted(collection)
    
    import string
    collection = random.choices(string.ascii_letters + string.digits, k=100)
    assert binary_insertion_sort(collection) == sorted(collection)
