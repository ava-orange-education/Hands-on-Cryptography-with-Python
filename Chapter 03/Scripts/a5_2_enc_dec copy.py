class A52Cipher:
    def __init__(self, key):
        # Convert the key to a list of bits
        self.key = [int(bit) for bit in bin(key)[2:].zfill(64)]

        # Initialize the LFSR
        self.lfsr = self.key[:19]

    def clock(self):
        # Perform one clock cycle on the LFSR
        feedback = self.lfsr[17] ^ self.lfsr[16] ^ self.lfsr[13] ^ self.lfsr[11] ^ self.lfsr[10] ^ self.lfsr[7] ^ self.lfsr[5] ^ self.lfsr[4] ^ self.lfsr[2] ^ self.lfsr[1] ^ self.lfsr[0]

        # Shift the bits in the LFSR
        self.lfsr = [feedback] + self.lfsr[:-1]

    def generate_keystream(self, length):
        # Generate keystream of specified length
        keystream = []

        for _ in range(length):
            output_bit = self.lfsr[18] ^ self.lfsr[16] ^ self.lfsr[13] ^ self.lfsr[11] ^ self.lfsr[10] ^ self.lfsr[7] ^ self.lfsr[5] ^ self.lfsr[4] ^ self.lfsr[2] ^ self.lfsr[1] ^ self.lfsr[0]
            keystream.append(output_bit)

            # Clock the LFSR
            self.clock()

        return keystream

    def encrypt(self, plaintext):
        # Convert the plaintext to a list of bits
        plaintext_bits = [int(bit) for bit in bin(plaintext)[2:].zfill(64)]

        # Generate keystream
        keystream = self.generate_keystream(len(plaintext_bits))

        # XOR the plaintext with the keystream to get the ciphertext
        ciphertext = [plaintext_bit ^ keystream_bit for plaintext_bit, keystream_bit in zip(plaintext_bits, keystream)]

        # Convert the ciphertext back to an integer
        ciphertext_int = int(''.join(map(str, ciphertext)), 2)

        return ciphertext_int

    def decrypt(self, ciphertext):
        # Decryption is the same as encryption in A5/2
        return self.encrypt(ciphertext)


# Example Usage:
key_a5_2 = 0x0123456789ABCDEF  # 64-bit key
plaintext_a5_2 = 0x123456789ABCDEF0  # 64-bit plaintext

a52_cipher = A52Cipher(key_a5_2)
ciphertext_a5_2 = a52_cipher.encrypt(plaintext_a5_2)
decrypted_text_a5_2 = a52_cipher.decrypt(ciphertext_a5_2)

print("Plaintext:", hex(plaintext_a5_2))
print("Encrypted:", hex(ciphertext_a5_2))
print("Decrypted:", hex(decrypted_text_a5_2))
