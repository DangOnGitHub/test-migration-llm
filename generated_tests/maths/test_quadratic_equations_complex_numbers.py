import pytest
from maths.quadratic_equations_complex_numbers import quadratic_roots

def test_quadratic_roots_real_roots():
    # 4.2x^2 + 8x + 1.9 = 0
    a = 4.2
    b = 8
    c = 1.9

    roots = quadratic_roots(a, b, c)
    assert len(roots) == 2
    assert roots[0] == pytest.approx(-0.27810465435684306)
    assert roots[1] == pytest.approx(-1.6266572504050616)

def test_quadratic_roots_equal_roots():
    # x^2 + 2x + 1 = 0
    a = 1
    b = 2
    c = 1

    roots = quadratic_roots(a, b, c)
    assert len(roots) == 2  # In Python, both roots are returned even if they are equal
    assert roots[0] == pytest.approx(-1)
    assert roots[1] == pytest.approx(-1)

def test_quadratic_roots_complex_roots():
    # 2.3x^2 + 4x + 5.6 = 0
    a = 2.3
    b = 4
    c = 5.6

    roots = quadratic_roots(a, b, c)
    assert len(roots) == 2
    assert roots[0] == pytest.approx(complex(-0.8695652173913044, 1.2956229935435948))
    assert roots[1] == pytest.approx(complex(-0.8695652173913044, -1.2956229935435948))