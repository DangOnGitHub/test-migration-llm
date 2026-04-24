import random
from sorts.stooge_sort import stooge_sort

def test_stooge_sort():
    # Test empty array
    assert stooge_sort([]) == []

    # Test single element array
    assert stooge_sort([1]) == [1]

    # Test two elements array
    assert stooge_sort([2, 1]) == [1, 2]
    assert stooge_sort([1, 2]) == [1, 2]

    # Test multiple elements array
    assert stooge_sort([3, 2, 1]) == [1, 2, 3]
    assert stooge_sort([5, 3, 2, 4, 1]) == [1, 2, 3, 4, 5]

    # Test array with duplicates
    assert stooge_sort([2, 2, 2, 1, 1]) == [1, 1, 2, 2, 2]

    # Test negative numbers
    assert stooge_sort([-1, -3, -2, -5]) == [-5, -3, -2, -1]

    # Test mixed positive and negative numbers
    assert stooge_sort([-1, 2, 0, -3, 5]) == [-3, -1, 0, 2, 5]

    # Test random large array
    random_array = [random.randint(-100, 100) for _ in range(1000)]
    sorted_array = sorted(random_array)
    assert stooge_sort(random_array) == sorted_array