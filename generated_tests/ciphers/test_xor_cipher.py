import pytest
from ciphers.xor_cipher import XORCipher

def test_xor_encrypt_decrypt():
    xor_cipher = XORCipher()
    plaintext = "My t&xt th@t will be ençrypted..."
    key = 256234  # Using an int key for XORCipher

    cipher_text = xor_cipher.encrypt_string(plaintext, key)
    decrypted_text = xor_cipher.decrypt_string(cipher_text, key)

    assert decrypted_text == "My t&xt th@t will be ençrypted..."

def test_empty_plaintext():
    xor_cipher = XORCipher()
    plaintext = ""
    key = 12345

    cipher_text = xor_cipher.encrypt_string(plaintext, key)
    decrypted_text = xor_cipher.decrypt_string(cipher_text, key)

    assert cipher_text == ""
    assert decrypted_text == ""

def test_empty_key():
    xor_cipher = XORCipher()
    plaintext = "Hello World!"
    key = 0

    with pytest.raises(AssertionError):
        assert xor_cipher.encrypt_string(plaintext, key)

    with pytest.raises(AssertionError):
        assert xor_cipher.decrypt_string(plaintext, key)

def test_short_key():
    xor_cipher = XORCipher()
    plaintext = "Short message"
    key = 1

    cipher_text = xor_cipher.encrypt_string(plaintext, key)
    decrypted_text = xor_cipher.decrypt_string(cipher_text, key)

    assert decrypted_text == plaintext

def test_non_ascii_characters():
    xor_cipher = XORCipher()
    plaintext = "こんにちは世界"  # "Hello World" in Japanese (Konichiwa Sekai)
    key = 5

    cipher_text = xor_cipher.encrypt_string(plaintext, key)
    decrypted_text = xor_cipher.decrypt_string(cipher_text, key)

    assert decrypted_text == plaintext

def test_same_key_and_plaintext():
    xor_cipher = XORCipher()
    plaintext = "samekey"
    key = 115

    cipher_text = xor_cipher.encrypt_string(plaintext, key)
    decrypted_text = xor_cipher.decrypt_string(cipher_text, key)

    assert decrypted_text == plaintext

def test_long_plaintext_short_key():
    xor_cipher = XORCipher()
    plaintext = "This is a long plaintext message."
    key = 25

    cipher_text = xor_cipher.encrypt_string(plaintext, key)
    decrypted_text = xor_cipher.decrypt_string(cipher_text, key)

    assert decrypted_text == plaintext