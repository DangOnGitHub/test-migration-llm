import pytest
from strings.reverse_letters import reverse_letters

@pytest.mark.parametrize("input_sentence, length, expected_output", [
    ("Hey wollef sroirraw", 3, "Hey fellow warriors"),
    ("nohtyP is nohtyP", 2, "Python is Python"),
    ("1 12 123 1234 54321 654321", 0, "1 21 321 4321 12345 123456"),
    ("racecar", 0, "racecar"),
    ("", 0, ""),
    ("A", 0, "A"),
    ("ab", 1, "ba"),
    ("  leading and trailing spaces  ", 5, "  gnidael and gniliart secaps  "),
    ("!@#$%^&*()", 0, ")(*&^%$#@!"),
    ("MixOf123AndText!", 3, "xiM123dnAeTtx!"),
])
def test_reverse_letters(input_sentence, length, expected_output):
    result = reverse_letters(input_sentence, length)
    assert result == expected_output

def test_reverse_letters_length_default():
    result = reverse_letters("racecar")
    assert result == "racecar"

if __name__ == "__main__":
    pytest.main()