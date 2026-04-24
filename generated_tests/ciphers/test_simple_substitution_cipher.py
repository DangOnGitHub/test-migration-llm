import pytest
from ciphers.simple_substitution_cipher import encrypt_message, decrypt_message

def test_simple_sub_cipher_encrypt():
    # given
    text = "defend the east wall of the castle"
    cipher_small = "phqgiumeaylnofdxjkrcvstzwb"

    # when
    cipher_text = encrypt_message(cipher_small.upper(), text)

    # then
    assert cipher_text == "giuifg cei iprc tpnn du cei qprcni"

def test_simple_sub_cipher_decrypt():
    # given
    encrypted_text = "giuifg cei iprc tpnn du cei qprcni"
    cipher_small = "phqgiumeaylnofdxjkrcvstzwb"

    # when
    decrypted_text = decrypt_message(cipher_small.upper(), encrypted_text)

    # then
    assert decrypted_text == "defend the east wall of the castle"
