from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

# Sample plaintext and secret key
plaintext = b'This is a secret message'
secret_key = get_random_bytes(16)  # AES-128 key

# Create an AES cipher object in ECB mode
cipher = AES.new(secret_key, AES.MODE_ECB)

# Encrypt the plaintext
cipher_text = cipher.encrypt(pad(plaintext, AES.block_size))

# Print the ciphertext
print("Ciphertext:", cipher_text)
