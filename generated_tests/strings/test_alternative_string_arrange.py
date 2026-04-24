import pytest
from strings.alternative_string_arrange import alternative_string_arrange

# Method to provide test data
def test_data():
    return [
        ("abc", "12345", "a1b2c345"),
        ("abcd", "12", "a1b2cd"),
        ("", "123", "123"),
        ("abc", "", "abc"),
        ("a", "1", "a1"),
        ("ab", "12", "a1b2"),
        ("abcdef", "123", "a1b2c3def"),
        ("ab", "123456", "a1b23456"),
    ]

@pytest.mark.parametrize("input1, input2, expected", test_data())
def test_alternative_string_arrange(input1, input2, expected):
    assert alternative_string_arrange(input1, input2) == expected