import pytest
from matrix.inverse_of_matrix import inverse_of_matrix

@pytest.mark.parametrize("matrix, expected_inverse", [
    ([[1, 0, 0], [0, 1, 0], [0, 0, 1]], [[1, 0, 0], [0, 1, 0], [0, 0, 1]]),
    ([[4, 7], [2, 6]], [[0.6, -0.7], [-0.2, 0.4]])
])
def test_inverse_of_matrix(matrix, expected_inverse):
    result = inverse_of_matrix(matrix)
    assert_matrix_equals(expected_inverse, result, 1.0E-10)

def assert_matrix_equals(expected, actual, tol):
    assert len(expected) == len(actual), "Matrix rows do not match"
    assert all(len(expected[i]) == len(actual[i]) for i in range(len(expected))), "Matrix columns do not match"
    for i, (expected_row, actual_row) in enumerate(zip(expected, actual)):
        for j, (ev, av) in enumerate(zip(expected_row, actual_row)):
            assert abs(ev - av) <= tol, f"Matrix value at row {i}, column {j} does not match"