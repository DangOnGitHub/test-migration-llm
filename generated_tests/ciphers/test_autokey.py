import pytest
from ciphers.autokey import encrypt, decrypt

def test_autokey_encrypt():
    # given
    plaintext = "MEET AT DAWN"
    keyword = "QUEEN"

    # when
    cipher_text = encrypt(plaintext, keyword)

    # then
    assert cipher_text == "cyixnfhepn"

def test_autokey_decrypt():
    # given
    ciphertext = "CYIX NF HEPN"
    keyword = "QUEEN"

    # when
    plain_text = decrypt(ciphertext, keyword)

    # then
    assert plain_text == "meetatdawn"