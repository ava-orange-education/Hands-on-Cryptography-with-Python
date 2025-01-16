def rc4_key_schedule(key):
    key_len = len(key)
    S = list(range(256))
    j = 0

    for i in range(256):
        j = (j + S[i] + key[i % key_len]) % 256
        S[i], S[j] = S[j], S[i]

    return S

def rc4_encrypt(plaintext, key):
    S = rc4_key_schedule(key)
    i = j = 0
    ciphertext = []

    for char in plaintext:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        k = S[(S[i] + S[j]) % 256]
        ciphertext.append(ord(char) ^ k)

    return bytes(ciphertext)

def rc4_decrypt(ciphertext, key):
    # Decryption is the same as encryption in RC4
    return rc4_encrypt(ciphertext, key)

# Example Usage:
plaintext = "Hello, RC4!"
key = "SecretKey"

encrypted_text = rc4_encrypt(plaintext, key)
decrypted_text = rc4_decrypt(encrypted_text, key)

print("Plaintext:", plaintext)
print("Encrypted:", encrypted_text)
print("Decrypted:", decrypted_text.decode('utf-8'))
