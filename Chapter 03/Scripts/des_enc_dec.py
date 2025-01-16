from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

def des_encrypt(plaintext, key):
    cipher = DES.new(key, DES.MODE_ECB)
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext

def des_decrypt(ciphertext, key):
    cipher = DES.new(key, DES.MODE_ECB)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext

# Sample plaintext and key
plaintext = b'This is a secret'
key = get_random_bytes(8)  # 8 bytes key for DES

# Encryption
encrypted = des_encrypt(plaintext, key)
print("Encrypted:", encrypted)

# Decryption
decrypted = des_decrypt(encrypted, key)
print("Decrypted:", decrypted)
