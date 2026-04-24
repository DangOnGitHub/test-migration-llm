import pytest
from ciphers.vigenere_cipher import encrypt_message, decrypt_message

def test_vigenere_encrypt_decrypt():
    text = "Hello World!"
    key = "suchsecret"

    encrypted_text = encrypt_message(key, text)
    decrypted_text = decrypt_message(key, encrypted_text)

    assert encrypted_text == "Zynsg Aqipw!"
    assert decrypted_text == "Hello World!"

def test_with_empty_message():
    text = ""
    key = "anykey"

    encrypted_text = encrypt_message(key, text)
    decrypted_text = decrypt_message(key, encrypted_text)

    assert encrypted_text == ""
    assert decrypted_text == ""

def test_with_empty_key():
    text = "This should remain the same"
    key = ""

    with pytest.raises(ValueError):
        encrypt_message(key, text)
    
    with pytest.raises(ValueError):
        decrypt_message(key, text)

def test_with_numbers_in_message():
    text = "Vigenere123!"
    key = "cipher"

    encrypted_text = encrypt_message(key, text)
    decrypted_text = decrypt_message(key, encrypted_text)

    assert encrypted_text == "Xqvlrvtm123!"
    assert decrypted_text == text

def test_longer_key_than_message():
    text = "Short"
    key = "VeryLongSecretKey"

    encrypted_text = encrypt_message(key, text)
    decrypted_text = decrypt_message(key, encrypted_text)

    assert encrypted_text == "Nlfpe"
    assert decrypted_text == text

def test_uppercase_message_and_key():
    text = "HELLO"
    key = "SECRET"

    encrypted_text = encrypt_message(key, text)
    decrypted_text = decrypt_message(key, encrypted_text)

    assert encrypted_text == "ZINCS"
    assert decrypted_text == text