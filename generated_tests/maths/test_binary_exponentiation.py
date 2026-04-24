import pytest
from maths.binary_exponentiation import (
    binary_exp_recursive,
    binary_exp_iterative,
    binary_exp_mod_recursive,
    binary_exp_mod_iterative,
)

def test_binary_exp_recursive():
    assert binary_exp_recursive(2, 2) == 4
    assert binary_exp_recursive(4, 4) == 256
    assert binary_exp_recursive(9, 3) == 729
    assert binary_exp_recursive(2, 0) == 1
    assert binary_exp_recursive(100, 0) == 1
    assert binary_exp_recursive(-5, 0) == 1
    assert binary_exp_recursive(0, 5) == 0
    assert binary_exp_recursive(0, 0) == 1
    assert binary_exp_recursive(1, 100) == 1
    assert binary_exp_recursive(1, 0) == 1
    assert binary_exp_recursive(-2, 3) == -8
    assert binary_exp_recursive(-2, 4) == 16
    assert binary_exp_recursive(2, 30) == 1073741824

def test_binary_exp_iterative():
    assert binary_exp_iterative(2, 2) == 4
    assert binary_exp_iterative(4, 4) == 256
    assert binary_exp_iterative(9, 3) == 729
    assert binary_exp_iterative(2, 0) == 1
    assert binary_exp_iterative(100, 0) == 1
    assert binary_exp_iterative(-5, 0) == 1
    assert binary_exp_iterative(0, 5) == 0
    assert binary_exp_iterative(0, 0) == 1
    assert binary_exp_iterative(1, 100) == 1
    assert binary_exp_iterative(1, 0) == 1
    assert binary_exp_iterative(-2, 3) == -8
    assert binary_exp_iterative(-2, 4) == 16
    assert binary_exp_iterative(2, 30) == 1073741824