import pytest
from strings.is_isogram import is_isogram

# Helper to define test cases
@pytest.fixture(params=[
    # Valid isograms (only checks letters)
    ("uncopyrightable", True), ("dermatoglyphics", True), ("background", True), ("python", True), ("keyboard", True), ("clipboard", True), ("flowchart", True),
    ("bankruptcy", True), ("computer", True), ("algorithms", True),

    # Not isograms - letters repeat
    ("hello", False), ("programming", False), ("java", False), ("coffee", False), ("book", False), ("letter", False), ("mississippi", False),
    ("google", False),

    # Edge cases
    ("", True), ("a", True), ("ab", True), ("abc", True), ("aa", False), ("abcdefghijklmnopqrstuvwxyz", True),

    # Case insensitive
    ("Python", True), ("BACKGROUND", True), ("Hello", False), ("PROGRAMMING", False)
])
def alphabetic_isogram_cases(request):
    return request.param

@pytest.fixture(params=[
    # Valid isograms (checks all characters)
    ("uncopyrightable", True), ("dermatoglyphics", True), ("background", True), ("python", True), ("keyboard", True), ("clipboard", True), ("flowchart", True),
    ("bankruptcy", True), ("computer", True), ("algorithms", True),

    # Not isograms - characters repeat
    ("hello", False), ("programming", False), ("java", False), ("coffee", False), ("book", False), ("letter", False), ("mississippi", False),
    ("google", False),

    # Edge cases
    ("", True), ("a", True), ("ab", True), ("abc", True), ("aa", False), ("abcdefghijklmnopqrstuvwxyz", True),

    # Case insensitive
    ("Python", True), ("BACKGROUND", True), ("Hello", False), ("PROGRAMMING", False),

    # Strings with symbols and numbers
    ("abc@def", True), # all characters unique
    ("test-case", False), # 't', 's', 'e' repeat
    ("python123", True), # all characters unique
    ("hello@123", False), # 'l' repeats
    ("abc123!@#", True), # all characters unique
    ("test123test", False), # 't', 'e', 's' repeat
    ("1234567890", True), # all digits unique
    ("12321", False), # '1' and '2' repeat
    ("!@#$%^&*()", True) # all special characters unique
])
def full_isogram_cases(request):
    return request.param

def test_is_isogram_with_alphabetic_isogram(alphabetic_isogram_cases):
    input_str, expected = alphabetic_isogram_cases
    if any(char.isdigit() or not char.isalpha() for char in input_str):
        with pytest.raises(ValueError):
            assert is_isogram(input_str)
    else:
        assert is_isogram(input_str) == expected

def test_is_isogram_with_full_isogram(full_isogram_cases):
    input_str, expected = full_isogram_cases
    try:
        result = is_isogram(input_str)
    except ValueError:
        result = False
    assert result == expected

def test_is_isogram_raises_exception():
    with pytest.raises(ValueError):
        is_isogram("1")
    with pytest.raises(ValueError):
        is_isogram("@")
    with pytest.raises(ValueError):
        is_isogram("python!")
    with pytest.raises(ValueError):
        is_isogram("123algorithm")
    with pytest.raises(ValueError):
        is_isogram("hello123")
    with pytest.raises(ValueError):
        is_isogram("!@@#$%^&*()")