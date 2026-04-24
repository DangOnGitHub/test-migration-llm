import pytest
from strings.upper import upper

def test_upper():
    assert upper("hello world") == "HELLO WORLD"
    assert upper("hElLo WoRlD") == "HELLO WORLD"
    assert upper("HELLO WORLD") == "HELLO WORLD"

if __name__ == "__main__":
    pytest.main()