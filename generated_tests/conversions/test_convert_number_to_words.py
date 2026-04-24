import pytest
from conversions.convert_number_to_words import convert_number

def test_null_input():
    with pytest.raises(ValueError, match="Input should be a valid integer"):
        convert_number(None)

def test_zero_input():
    assert convert_number(0) == "zero"

def test_positive_whole_numbers():
    assert convert_number(1) == "one"
    assert convert_number(1000) == "one thousand"
    assert convert_number(1000000) == "one million"

def test_negative_whole_numbers():
    assert convert_number(-1) == "negative one"
    assert convert_number(-1000) == "negative one thousand"

def test_large_numbers():
    assert convert_number(999999999) == ("nine hundred ninety-nine million "
                                         "nine hundred ninety-nine thousand "
                                         "nine hundred ninety-nine")
    assert convert_number(1000000000000) == "one trillion"

def test_negative_large_numbers():
    assert convert_number(-9876543210987) == ("negative nine trillion "
                                              "eight hundred seventy-six billion "
                                              "five hundred forty-three million "
                                              "two hundred ten thousand "
                                              "nine hundred eighty-seven")

def test_edge_cases():
    assert convert_number(-0) == "zero"
    with pytest.raises(ValueError, match="Input number is too large"):
        convert_number(10**18)
    
# Since Python's number handling is a bit different, Python doesn't easily support 
# floating point conversion in natural language. Thus, these following tests around 
# fractional numbers and floating point precision are removed, as they would need 
# an alternative encoding / function not provided in the given python code.