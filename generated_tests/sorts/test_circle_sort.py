import pytest
from sorts.circle_sort import circle_sort

def test_circle_sort():
    assert circle_sort([0, 5, 3, 2, 2]) == [0, 2, 2, 3, 5]
    assert circle_sort([]) == []
    assert circle_sort([-2, 5, 0, -45]) == [-45, -2, 0, 5]
    collections = [
        [],
        [0, 5, 3, 2, 2],
        [-2, 5, 0, -45],
        [5, 1, 4, 2, 8, 0, 2],
        [10],
        [9, 7],
        [-3, -3, -3],
        [3, 3, 3, 3, 3]
    ]
    for collection in collections:
        assert circle_sort(collection) == sorted(collection)

if __name__ == "__main__":
    pytest.main()