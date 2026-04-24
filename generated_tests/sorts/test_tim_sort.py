import pytest
from sorts.tim_sort import tim_sort

def test_tim_sort():
    assert tim_sort([5, 9, 10, 3, -4, 5, 178, 92, 46, -18, 0, 7]) == sorted([5, 9, 10, 3, -4, 5, 178, 92, 46, -18, 0, 7])
    assert tim_sort("Python") == sorted("Python")
    assert tim_sort((1.1, 1, 0, -1, -1.1)) == sorted((1.1, 1, 0, -1, -1.1))
    assert tim_sort(list(reversed(list(range(7))))) == sorted(list(reversed(list(range(7)))))
    assert tim_sort([3, 2, 1]) == sorted([3, 2, 1])

if __name__ == "__main__":
    pytest.main()