import pytest
from maths.twin_prime import twin_prime

def test_should_return_7():
    # given
    number = 5
    expected_result = 7

    # when
    actual_result = twin_prime(number)

    # then
    assert expected_result == actual_result

def test_should_return_5():
    # given
    number = 3
    expected_result = 5

    # when
    actual_result = twin_prime(number)

    # then
    assert expected_result == actual_result

def test_should_return_negative_1():
    # given
    number = 4
    expected_result = -1

    # when
    actual_result = twin_prime(number)

    # then
    assert expected_result == actual_result

def test_should_return_19():
    # given
    number = 17
    expected_result = 19

    # when
    actual_result = twin_prime(number)

    # then
    assert expected_result == actual_result