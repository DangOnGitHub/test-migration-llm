import pytest
from strings.check_anagrams import check_anagrams

@pytest.mark.parametrize("input1, input2, expected", [
    ("late", "tale", True),
    ("late", "teal", True),
    ("listen", "silent", True),
    ("hello", "olelh", True),
    ("hello", "world", False),
    ("deal", "lead", True),
    ("binary", "brainy", True),
    ("adobe", "abode", True),
    ("cat", "act", True),
    ("cat", "cut", False),
    ("Listen", "Silent", True),
    ("Dormitory", "DirtyRoom", True),
    ("Schoolmaster", "TheClassroom", True),
    ("Astronomer", "MoonStarer", True),
    ("Conversation", "VoicesRantOn", True)
])
def test_check_anagrams(input1, input2, expected):
    assert check_anagrams(input1, input2) == expected