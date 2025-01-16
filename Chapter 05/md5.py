import struct

def left_rotate(x, amount):
    return ((x << amount) & 0xFFFFFFFF) | (x >> (32 - amount))

def md5_padding(message):
    original_length = (8 * len(message)) & 0xFFFFFFFFFFFFFFFF
    message += b'\x80'
    message += b'\x00' * ((56 - (len(message) % 64)) % 64)
    message += struct.pack('<Q', original_length)
    return message

def md5(message):
    # Constants for MD5
    s = [7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22,
         5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20,
         4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23,
         6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21]

    K = [0xD76AA478, 0xE8C7B756, 0x242070DB, 0xC1BDCEEE,
         0xF57C0FAF, 0x4787C62A, 0xA8304613, 0xFD469501,
         0x698098D8, 0x8B44F7AF, 0xFFFF5BB1, 0x895CD7BE,
         0x6B901122, 0xFD987193, 0xA679438E, 0x49B40821,
         0xF61E2562, 0xC040B340, 0x265E5A51, 0xE9B6C7AA,
         0xD62F105D, 0x02441453, 0xD8A1E681, 0xE7D3FBC8,
         0x21E1CDE6, 0xC33707D6, 0xF4D50D87, 0x455A14ED,
         0xA9E3E905, 0xFCEFA3F8, 0x676F02D9, 0x8D2A4C8A,
         0xFFFA3942, 0x8771F681, 0x6D9D6122, 0xFDE5380C,
         0xA4BEEA44, 0x4BDECFA9, 0xF6BB4B60, 0xBEBFBC70,
         0x289B7EC6, 0xEAA127FA, 0xD4EF3085, 0x04881D05,
         0xD9D4D039, 0xE6DB99E5, 0x1FA27CF8, 0xC4AC5665,
         0xF4292244, 0x432AFF97, 0xAB9423A7, 0xFC93A039,
         0x655B59C3, 0x8F0CCC92, 0xFFEFF47D, 0x85845DD1,
         0x6FA87E4F, 0xFE2CE6E0, 0xA3014314, 0x4E0811A1,
         0xF7537E82, 0xBD3AF235, 0x2AD7D2BB, 0xEB86D391]

    # Initial hash values
    A, B, C, D = 0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476

    # Process each 512-bit block
    for chunk_start in range(0, len(message), 64):
        chunk = message[chunk_start:chunk_start + 64]

        # Break chunk into sixteen 32-bit words
        M = struct.unpack('<16I', chunk)

        # Initialize hash values for this chunk
        a, b, c, d = A, B, C, D

        # Main loop
        for i in range(64):
            if i < 16:
                F = (b & c) | ((~b) & d)
                g = i
            elif i < 32:
                F = (d & b) | ((~d) & c)
                g = (5 * i + 1) % 16
            elif i < 48:
                F = b ^ c ^ d
                g = (3 * i + 5) % 16
            else:
                F = c ^ (b | (~d))
                g = (7 * i) % 16

            # Update hash values
            temp = d
            d = c
            c = b
            b = (b + left_rotate((a + F + K[i] + M[g]) & 0xFFFFFFFF, s[i])) & 0xFFFFFFFF
            a = temp

        # Update hash values for this chunk
        A = (A + a) & 0xFFFFFFFF
        B = (B + b) & 0xFFFFFFFF
        C = (C + c) & 0xFFFFFFFF
        D = (D + d) & 0xFFFFFFFF

    # Concatenate hash values
    digest = struct.pack('<4I', A, B, C, D)
    return digest

# Example Usage
message = b"Hello, World!"
print("Message: ", message)
hashed_message = md5(md5_padding(message))
print("Md5: ",hashed_message.hex())
