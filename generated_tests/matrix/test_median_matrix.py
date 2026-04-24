import pytest
from matrix.median_matrix import median

def test_median_with_odd_number_of_elements():
    matrix = [
        [1, 3, 5],
        [2, 4, 6],
        [7, 8, 9]
    ]
    
    result = median(matrix)
    assert result == 5

def test_median_with_even_number_of_elements():
    matrix = [
        [2, 4],
        [1, 3]
    ]
    
    result = median(matrix)
    assert result == 2

def test_median_single_element():
    matrix = [
        [1]
    ]
    
    result = median(matrix)
    assert result == 1

def test_empty_matrix_raises_exception():
    with pytest.raises(ValueError, match="Matrix must contain at least one element."):
        median([])