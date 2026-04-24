import pytest
from ciphers.caesar_cipher import encrypt, decrypt, brute_force

def test_caesar_encrypt():
    # given
    text_to_encrypt = "Encrypt this text"
    # when
    cipher_text = encrypt(text_to_encrypt, 5)
    # then
    assert cipher_text == "Jshwduy ymnx yjcy"

def test_caesar_decrypt():
    # given
    encrypted_text = "Jshwduy ymnx yjcy"
    # when
    plain_text = decrypt(encrypted_text, 5)
    # then
    assert plain_text == "Encrypt this text"

def test_caesar_brute_force():
    # given
    encrypted_text = "Jshwduy ymnx yjcy"
    # when
    all_possible_answers = brute_force(encrypted_text)
    # then
    assert len(all_possible_answers) == 52
    assert all_possible_answers[5] == "Encrypt this text"