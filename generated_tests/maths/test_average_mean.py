import pytest
from math import sqrt
from typing import List

EPSILON = 1e-9

def arithmetic(numbers: List[float]) -> float:
    if not numbers:
        raise ValueError("Empty list given for Mean computation.")
    return sum(numbers) / len(numbers)

def geometric(numbers: List[float]) -> float:
    if not numbers:
        raise ValueError("Empty list given for Mean computation.")
    product = 1.0
    for x in numbers:
        product *= x
    return product ** (1.0 / len(numbers))

def harmonic(numbers: List[float]) -> float:
    if not numbers:
        raise ValueError("Empty list given for Mean computation.")
    reciprocal_sum = sum(1.0 / x for x in numbers)
    return len(numbers) / reciprocal_sum

def quadratic(numbers: List[float]) -> float:
    if not numbers:
        raise ValueError("Empty list given for Mean computation.")
    sum_of_squares = sum(x * x for x in numbers)
    return sqrt(sum_of_squares / len(numbers))

# ========== Arithmetic Mean Tests ==========

def test_arithmetic_mean_throws_exception_for_empty_list():
    with pytest.raises(ValueError, match="Empty list"):
        arithmetic([])

def test_arithmetic_mean_single_number():
    assert abs(arithmetic([2.5]) - 2.5) < EPSILON

def test_arithmetic_mean_two_numbers():
    assert abs(arithmetic([2.0, 4.0]) - 3.0) < EPSILON

def test_arithmetic_mean_multiple_numbers():
    assert abs(arithmetic([1.0, 2.0, 3.0, 4.0, 5.0]) - 3.0) < EPSILON

def test_arithmetic_mean_with_negative_numbers():
    assert abs(arithmetic([-5.0, -3.0, -1.0, 1.0, 3.0, 5.0]) - 0.0) < EPSILON

def test_arithmetic_mean_with_decimal_numbers():
    assert abs(arithmetic([1.1, 2.2, 3.3, 4.4, 5.5]) - 3.3) < EPSILON

# ========== Geometric Mean Tests ==========

def test_geometric_mean_throws_exception_for_empty_list():
    with pytest.raises(ValueError, match="Empty list"):
        geometric([])

def test_geometric_mean_single_number():
    assert abs(geometric([2.5]) - 2.5) < EPSILON

def test_geometric_mean_two_numbers():
    assert abs(geometric([2.0, 8.0]) - 4.0) < EPSILON

def test_geometric_mean_multiple_numbers():
    assert abs(geometric([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 1.25]) - 2.6426195539300585) < EPSILON

def test_geometric_mean_identical_numbers():
    assert abs(geometric([5.0, 5.0, 5.0, 5.0]) - 5.0) < EPSILON

# ========== Harmonic Mean Tests ==========

def test_harmonic_mean_throws_exception_for_empty_list():
    with pytest.raises(ValueError, match="Empty list"):
        harmonic([])

def test_harmonic_mean_single_number():
    assert abs(harmonic([2.5]) - 2.5) < EPSILON

def test_harmonic_mean_two_numbers():
    expected = 2.0 / (1.0 / 2.0 + 1.0 / 4.0)
    assert abs(harmonic([2.0, 4.0]) - expected) < EPSILON

def test_harmonic_mean_multiple_numbers():
    assert abs(harmonic([1.0, 2.5, 83.3, 25.9999, 46.0001, 74.7, 74.5]) - 4.6697322801074135) < EPSILON

def test_harmonic_mean_identical_numbers():
    assert abs(harmonic([6.0, 6.0, 6.0]) - 6.0) < EPSILON

# ========== Quadratic Mean Tests ==========

def test_quadratic_mean_throws_exception_for_empty_list():
    with pytest.raises(ValueError, match="Empty list"):
        quadratic([])

def test_quadratic_mean_single_number():
    assert abs(quadratic([2.5]) - 2.5) < EPSILON

def test_quadratic_mean_two_numbers():
    assert abs(quadratic([1.0, 7.0]) - 5.0) < EPSILON

def test_quadratic_mean_multiple_numbers():
    expected = sqrt(34.5)
    assert abs(quadratic([1.0, 2.5, 3.0, 7.5, 10.0]) - expected) < EPSILON

def test_quadratic_mean_identical_numbers():
    assert abs(quadratic([5.0, 5.0, 5.0]) - 5.0) < EPSILON

# ========== Additional Edge Case Tests ==========

def test_arithmetic_mean_with_very_large_numbers():
    assert abs(arithmetic([1e100, 2e100, 3e100]) - 2e100) < 1e90

def test_arithmetic_mean_with_very_small_numbers():
    assert abs(arithmetic([1e-100, 2e-100, 3e-100]) - 2e-100) < 1e-110

def test_geometric_mean_with_ones():
    assert abs(geometric([1.0, 1.0, 1.0, 1.0]) - 1.0) < EPSILON

def test_all_means_consistency_for_identical_values():
    numbers = [7.5, 7.5, 7.5, 7.5]
    arithmetic_mean = arithmetic(numbers)
    geometric_mean = geometric(numbers)
    harmonic_mean = harmonic(numbers)
    quadratic_mean = quadratic(numbers)

    assert abs(arithmetic_mean - 7.5) < EPSILON
    assert abs(geometric_mean - 7.5) < EPSILON
    assert abs(harmonic_mean - 7.5) < EPSILON
    assert abs(quadratic_mean - 7.5) < EPSILON

def test_means_relationship():
    numbers = [2.0, 4.0, 8.0]
    harmonic_mean = harmonic(numbers)
    geometric_mean = geometric(numbers)
    arithmetic_mean = arithmetic(numbers)
    quadratic_mean = quadratic(numbers)

    assert harmonic_mean <= geometric_mean
    assert geometric_mean <= arithmetic_mean
    assert arithmetic_mean <= quadratic_mean