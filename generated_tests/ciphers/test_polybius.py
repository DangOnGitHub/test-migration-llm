import numpy as np
from ciphers.polybius import PolybiusCipher

def test_encode():
    # Given
    plaintext = "HELLOWORLD"

    # When
    actual = PolybiusCipher().encode(plaintext)

    # Then
    assert actual == "23153131542325325443"

def test_decode():
    # Given
    ciphertext = "23153131542325325443"

    # When
    actual = PolybiusCipher().decode(ciphertext)

    # Then
    assert actual == "helloworld"

def test_is_text_the_same_after_encoding_and_decoding():
    # Given
    plaintext = "HELLOWORLD"

    # When
    encoded_text = PolybiusCipher().encode(plaintext)
    actual = PolybiusCipher().decode(encoded_text)

    # Then
    assert actual == plaintext.lower()