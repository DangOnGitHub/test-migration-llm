import pytest
from strings.rabin_karp import rabin_karp

def test_null_inputs():
    assert not rabin_karp(None, "A")
    assert not rabin_karp("A", None)
    assert not rabin_karp(None, None)

def test_hash_collision():
    collision_char = chr(198)
    text = str(collision_char)
    pattern = "a"
    assert not rabin_karp(pattern, text)

def test_rabin_karp_search():
    assert rabin_karp("AAAAABAAABA", "AAAA")
    assert rabin_karp("ABCABC", "ABC")
    assert rabin_karp("ABABDABACDABABCABAB", "ABABCABAB")
    assert not rabin_karp("ABCDE", "FGH")
    assert not rabin_karp("A", "AA")
    assert rabin_karp("AAA", "A")
    assert rabin_karp("A", "A")
    assert not rabin_karp("", "A")
    assert not rabin_karp("A", "")