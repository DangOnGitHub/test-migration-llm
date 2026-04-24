from ciphers.baconian_cipher import encode, decode

def test_baconian_cipher_encode():
    # given
    plaintext = "MEET AT DAWN"
    
    # when
    cipher_text = encode(plaintext)
    
    # then
    assert cipher_text == "ABBAAAABAAAABAABAABBAAAAABAABBAAABBAAAAABABBAABBAB"

def test_baconian_cipher_decode():
    # given
    ciphertext = "ABBAAAABAAAABAABAABBAAAAABAABBAAABBAAAAABABBAABBAB"
    
    # when
    plain_text = decode(ciphertext)
    
    # then
    assert plain_text == "meet at dawn"