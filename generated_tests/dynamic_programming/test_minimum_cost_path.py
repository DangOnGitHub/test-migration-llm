import pytest
from dynamic_programming.minimum_cost_path import minimum_cost_path

def test_minimum_cost_path_with_regular_grid():
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    assert minimum_cost_path(grid) == 7

def test_minimum_cost_path_with_one_row_one_column_grid():
    grid = [[2]]
    assert minimum_cost_path(grid) == 2

def test_minimum_cost_path_with_empty_grid():
    grid = [[]]
    assert minimum_cost_path(grid) == 0

def test_minimum_cost_path_with_one_column_grid():
    grid = [[1], [2], [3]]
    assert minimum_cost_path(grid) == 6

def test_minimum_cost_path_with_one_row_grid():
    grid = [[1, 2, 3]]
    assert minimum_cost_path(grid) == 6

def test_minimum_cost_path_with_diff_row_and_column_grid():
    grid = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    assert minimum_cost_path(grid) == 30

def test_minimum_cost_path_with_negative_number_grid():
    grid = [[1, 3, 1], [3, 4, 1], [4, -3, 1]]
    assert minimum_cost_path(grid) == 6

if __name__ == '__main__':
    pytest.main()