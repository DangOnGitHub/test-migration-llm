import pytest
from sorts.cocktail_shaker_sort import cocktail_shaker_sort

@pytest.mark.parametrize("unsorted, expected", [
    ([4, 5, 2, 1, 2], [1, 2, 2, 4, 5]),
    ([-4, 5, 0, 1, 2, 11], [-4, 0, 1, 2, 5, 11]),
    ([0.1, -2.4, 4.4, 2.2], [-2.4, 0.1, 2.2, 4.4]),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([-4, -5, -24, -7, -11], [-24, -11, -7, -5, -4]),
    (["elderberry", "banana", "date", "apple", "cherry"], ["apple", "banana", "cherry", "date", "elderberry"]),
])
def test_cocktail_shaker_sort(unsorted, expected):
    assert cocktail_shaker_sort(unsorted) == expected

def test_cocktail_shaker_sort_type_error_on_tuple():
    with pytest.raises(TypeError):
        cocktail_shaker_sort((-4, -5, -24, -7, -11))