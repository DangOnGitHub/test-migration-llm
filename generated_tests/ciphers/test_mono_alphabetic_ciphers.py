import pytest
from ciphers.mono_alphabetic_ciphers import encrypt_message, decrypt_message

@pytest.mark.parametrize("plain_text, key, encrypted_text", [
    ("HELLO", "MNBVCXZLKJHGFDSAPOIUYTREWQ", "LCGGS"),
    ("JAVA", "MNBVCXZLKJHGFDSAPOIUYTREWQ", "JMTM"),
    ("HELLO", "QWERTYUIOPLKJHGFDSAZXCVBNM", "ITKKG"),
    ("JAVA", "QWERTYUIOPLKJHGFDSAZXCVBNM", "PQCQ")
])
def test_encrypt_decrypt(plain_text, key, encrypted_text):
    # Test encryption
    actual_encrypted = encrypt_message(key, plain_text)
    assert actual_encrypted == encrypted_text, f"Encryption failed for input: {plain_text} with key: {key}"

    # Test decryption
    actual_decrypted = decrypt_message(key, encrypted_text)
    assert actual_decrypted == plain_text, f"Decryption failed for input: {encrypted_text} with key: {key}"