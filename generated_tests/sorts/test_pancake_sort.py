import pytest
from sorts.pancake_sort import pancake_sort

def test_pancake_sort():
    assert pancake_sort([0, 5, 3, 2, 2]) == [0, 2, 2, 3, 5]
    assert pancake_sort([]) == []
    assert pancake_sort([-2, -5, -45]) == [-45, -5, -2]
    assert pancake_sort([1]) == [1]
    assert pancake_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert pancake_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert pancake_sort([5, 3, 1, 4, 2]) == [1, 2, 3, 4, 5]

if __name__ == "__main__":
    pytest.main()