# Using the same secret key, create a new AES cipher object for decryption
cipher_decrypt = AES.new(secret_key, AES.MODE_ECB)

# Decrypt the ciphertext
decrypted_text = unpad(cipher_decrypt.decrypt(cipher_text), AES.block_size)

# Convert bytes to string for human-readable output
decrypted_text_str = decrypted_text.decode('utf-8')

# Print the decrypted plaintext
print("Decrypted Text:", decrypted_text_str)
