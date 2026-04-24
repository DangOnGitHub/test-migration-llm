import pytest
from maths.extended_euclidean_algorithm import extended_euclidean_algorithm

def verify_bezout_identity(a, b, result):
    x, y = result
    gcd = abs(a * x + b * y)
    expected_gcd = abs(a if b == 0 else b if a == 0 else gcd)
    assert gcd == expected_gcd, f"Bézout's identity failed for gcd({a}, {b})"

def test_extended_euclidean_algorithm():
    # Test case 1: General case gcd(30, 50) = 10
    result1 = extended_euclidean_algorithm(30, 50)
    assert abs(result1[0] * 30 + result1[1] * 50) == 10, "Test Case 1 Failed: gcd(30, 50) should be 10"
    verify_bezout_identity(30, 50, result1)

    # Test case 2: Another general case gcd(240, 46) = 2
    result2 = extended_euclidean_algorithm(240, 46)
    assert abs(result2[0] * 240 + result2[1] * 46) == 2, "Test Case 2 Failed: gcd(240, 46) should be 2"
    verify_bezout_identity(240, 46, result2)

    # Test case 3: Base case where b is 0, gcd(10, 0) = 10
    result3 = extended_euclidean_algorithm(10, 0)
    assert abs(result3[0] * 10 + result3[1] * 0) == 10, "Test Case 3 Failed: gcd(10, 0) should be 10"
    verify_bezout_identity(10, 0, result3)

    # Test case 4: Numbers are co-prime gcd(17, 13) = 1
    result4 = extended_euclidean_algorithm(17, 13)
    assert abs(result4[0] * 17 + result4[1] * 13) == 1, "Test Case 4 Failed: gcd(17, 13) should be 1"
    verify_bezout_identity(17, 13, result4)

    # Test case 5: One number is a multiple of the other gcd(100, 20) = 20
    result5 = extended_euclidean_algorithm(100, 20)
    assert abs(result5[0] * 100 + result5[1] * 20) == 20, "Test Case 5 Failed: gcd(100, 20) should be 20"
    verify_bezout_identity(100, 20, result5)