import pytest
from maths.geometric_mean import compute_geometric_mean

EPSILON = 1e-9

# ========== Geometric Mean Tests ==========

def test_geometric_mean_empty_list():
    with pytest.raises(TypeError):
        compute_geometric_mean()

def test_geometric_mean_single_number():
    assert abs(compute_geometric_mean(2.5) - 2.5) < EPSILON

def test_geometric_mean_two_numbers():
    assert abs(compute_geometric_mean(2, 8) - 4.0) < EPSILON

def test_geometric_mean_multiple_numbers():
    assert abs(compute_geometric_mean(1, 2, 3, 4, 5, 6, 1.25) - 2.6426195539300585) < EPSILON

def test_geometric_mean_perfect_squares():
    numbers = (1, 4, 9, 16)
    expected = (1 * 4 * 9 * 16) ** 0.25
    assert abs(compute_geometric_mean(*numbers) - expected) < EPSILON

def test_geometric_mean_identical_numbers():
    assert abs(compute_geometric_mean(5, 5, 5, 5) - 5.0) < EPSILON

def test_geometric_mean_with_ones():
    assert abs(compute_geometric_mean(1, 1, 1, 1) - 1.0) < EPSILON

def test_geometric_mean_arithmetic_error():
    with pytest.raises(ArithmeticError):
        compute_geometric_mean(2, -2)

# ========== Extra consistency and relationship tests ==========

def test_all_means_consistency_for_identical_values():
    numbers = (7.5, 7.5, 7.5, 7.5)
    geometric = compute_geometric_mean(*numbers)
    assert abs(geometric - 7.5) < EPSILON

@pytest.fixture
def positive_numbers():
    return (2.0, 4.0, 8.0)

def test_means_relationship(positive_numbers):
    geometric = compute_geometric_mean(*positive_numbers)
    harmonic = len(positive_numbers) / sum(1.0/n for n in positive_numbers)
    arithmetic = sum(positive_numbers) / len(positive_numbers)
    quadratic = (sum(n ** 2 for n in positive_numbers) / len(positive_numbers)) ** 0.5

    assert harmonic <= geometric
    assert geometric <= arithmetic
    assert arithmetic <= quadratic