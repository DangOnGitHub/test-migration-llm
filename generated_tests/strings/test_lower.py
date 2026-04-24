import pytest
from strings.lower import lower

def test_to_lower():
    input1 = "hello world"
    input2 = "HelLO WoRld"
    input3 = "HELLO WORLD"

    assert lower(input1) == "hello world"
    assert lower(input2) == "hello world"
    assert lower(input3) == "hello world"