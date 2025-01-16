class A51Cipher:
    def __init__(self, key):
        # Convert the key to a list of bits
        self.key = [int(bit) for bit in bin(key)[2:].zfill(64)]

        # Initialize the three LFSRs
        self.lfsr1 = self.key[:19]
        self.lfsr2 = self.key[19:41]
        self.lfsr3 = self.key[41:]

    def clock(self):
        # Perform one clock cycle on the three LFSRs
        feedback1 = self.lfsr1[18] ^ self.lfsr1[17] ^ self.lfsr1[16] ^ self.lfsr1[13]
        feedback2 = self.lfsr2[21] ^ self.lfsr2[20]
        feedback3 = self.lfsr3[22] ^ self.lfsr3[21]

        # Shift the bits in the LFSRs
        self.lfsr1 = [feedback1] + self.lfsr1[:-1]
        self.lfsr2 = [feedback2] + self.lfsr2[:-1]
        self.lfsr3 = [feedback3] + self.lfsr3[:-1]

    def generate_keystream(self, length):
        # Generate keystream of specified length
        keystream = []

        for _ in range(length):
            output_bit = self.lfsr1[18] ^ self.lfsr2[21] ^ self.lfsr3[22]
            keystream.append(output_bit)

            # Clock the LFSRs
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
        # Decryption is the same as encryption in A5/1
        return self.encrypt(ciphertext)


# Example Usage:
key = 0x0123456789ABCDEF  # 64-bit key
plaintext = 0x123456789ABCDEF0  # 64-bit plaintext

a51_cipher = A51Cipher(key)
ciphertext = a51_cipher.encrypt(plaintext)
decrypted_text = a51_cipher.decrypt(ciphertext)

print("Plaintext:", hex(plaintext))
print("Encrypted:", hex(ciphertext))
print("Decrypted:", hex(decrypted_text))