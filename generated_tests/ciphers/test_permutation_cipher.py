import pytest
from ciphers.permutation_cipher import encrypt, decrypt


def test_basic_encryption():
    plaintext = "HELLO"
    key = [2, 0, 1]  # Move 3rd position to 1st, 1st to 2nd, 2nd to 3rd
    encrypted, encryption_key = encrypt(plaintext, key=key, block_size=len(key))
    # HEL is "231" permuted to "CLH"
    # LOX is "231" permuted to "XOL"
    assert encrypted == "LHELOX"


def test_basic_decryption():
    ciphertext = "LHELOX"
    key = [2, 0, 1]
    decrypted = decrypt(ciphertext, key=key)
    assert decrypted == "HELLO"


def test_encrypt_decrypt_round_trip():
    plaintext = "THIS IS A TEST MESSAGE"
    key = [3, 1, 0, 2]
    encrypted, _ = encrypt(plaintext, key=key, block_size=len(key))
    decrypted = decrypt(encrypted, key)
    assert decrypted.replace(" ", "") == "THISISATESTMESSAGE"


def test_single_character_key():
    plaintext = "ABCDEF"
    key = [0]  # Identity permutation
    encrypted, _ = encrypt(plaintext, key=key, block_size=len(key))
    decrypted = decrypt(encrypted, key)
    assert encrypted == plaintext
    assert decrypted == plaintext


def test_larger_key():
    plaintext = "PERMUTATION"
    key = [4, 2, 0, 3, 1]
    encrypted, _ = encrypt(plaintext, key=key, block_size=len(key))
    decrypted = decrypt(encrypted, key)
    assert decrypted == plaintext


def test_exact_block_size():
    plaintext = "ABCDEF"  # Length 6, divisible by key length 3
    key = [1, 2, 0]
    encrypted, _ = encrypt(plaintext, key=key, block_size=len(key))
    decrypted = decrypt(encrypted, key)
    assert decrypted == plaintext


def test_empty_string():
    plaintext = ""
    key = [1, 0, 2]
    encrypted, _ = encrypt(plaintext, key=key, block_size=len(key))
    decrypted = decrypt(encrypted, key)
    assert encrypted == ""
    assert decrypted == ""


def test_string_with_spaces():
    plaintext = "A B C D E F"
    key = [1, 0]
    encrypted, _ = encrypt(plaintext, key=key, block_size=len(key))
    decrypted = decrypt(encrypted, key)
    assert decrypted.replace(" ", "") == "ABCDEF"


def test_lowercase_conversion():
    plaintext = "hello world"
    key = [2, 0, 1]
    encrypted, _ = encrypt(plaintext.upper(), key=key, block_size=len(key))
    decrypted = decrypt(encrypted, key)
    assert decrypted == "HELLOWORLD"


def test_invalid_key_empty():
    plaintext = "HELLO"
    with pytest.raises(ValueError):
        encrypt(plaintext, key=[], block_size=0)


def test_invalid_key_out_of_range():
    plaintext = "HELLO"
    with pytest.raises(ValueError):
        encrypt(plaintext, key=[0, 1, 3], block_size=3)


def test_invalid_key_zero():
    plaintext = "HELLO"
    with pytest.raises(ValueError):
        encrypt(plaintext, key=[0, 1, 2], block_size=3)


def test_invalid_key_duplicate():
    plaintext = "HELLO"
    with pytest.raises(ValueError):
        encrypt(plaintext, key=[0, 1, 1], block_size=3)


def test_invalid_key_missing_position():
    plaintext = "HELLO"
    with pytest.raises(ValueError):
        encrypt(plaintext, key=[0, 2], block_size=2)


def test_reverse_key():
    plaintext = "ABCD"
    key = [3, 2, 1, 0]
    encrypted, _ = encrypt(plaintext, key=key, block_size=len(key))
    decrypted = decrypt(encrypted, key)
    assert encrypted == "DCBA"
    assert decrypted == plaintext


def test_specific_example_from_description():
    plaintext = "HELLO"
    key = [2, 0, 1]
    encrypted, _ = encrypt(plaintext, key=key, block_size=len(key))
    assert encrypted == "LHELOX"
    decrypted = decrypt(encrypted, key)
    assert decrypted == "HELLO"


def test_long_text():
    plaintext = "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"
    key = [3, 0, 2, 1]
    encrypted, _ = encrypt(plaintext.replace(" ", ""), key=key, block_size=len(key))
    decrypted = decrypt(encrypted, key)
    assert decrypted == plaintext.replace(" ", "")


def test_identity_permutation():
    plaintext = "IDENTITY"
    key = [0, 1, 2, 3]
    encrypted, _ = encrypt(plaintext, key=key, block_size=len(key))
    decrypted = decrypt(encrypted, key)
    assert encrypted == plaintext
    assert decrypted == plaintext


def test_empty_string_remove_padding():
    ciphertext = ""
    key = [1, 0, 2]
    decrypted = decrypt(ciphertext, key)
    assert decrypted == ""


def test_block_shorter_than_key():
    malformed_ciphertext = "AB"  # Length 2, but key length is 3
    key = [2, 0, 1]  # Key length is 3
    # This should trigger the padding logic in permuteBlock during decryption
    decrypted = decrypt(malformed_ciphertext, key)
    # "AB" gets padded to "ABX", then permuted with inverse key which will be handled
    assert decrypted == "BA"