import pytest
from strings.reverse_words import reverse_words

@pytest.mark.parametrize("expected, input", [
    ("blue is Sky", "Sky is blue"),
    ("blue is Sky", "Sky \n is \t \n  blue "),
    ("", ""),
    ("", "    "),
    ("", "\t")
])
def test_reverse_words(expected, input):
    assert reverse_words(input) == expected