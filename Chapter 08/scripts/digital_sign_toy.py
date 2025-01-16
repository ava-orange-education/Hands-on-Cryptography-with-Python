import random
from hashlib import sha256

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    d = 0
    x1, x2, y1 = 0, 1, 1
    temp_phi = phi
    
    while e > 0:
        temp1 = temp_phi // e
        temp2 = temp_phi - temp1 * e
        temp_phi, e = e, temp2
        
        x = x2 - temp1 * x1
        y = d - temp1 * y1
        
        x2, x1 = x1, x
        d, y1 = y1, y
    
    if temp_phi == 1:
        return d + phi

def generate_key_pair(bits):
    p = get_prime(bits // 2)
    q = get_prime(bits // 2)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randrange(1, phi)
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)
    d = mod_inverse(e, phi)
    return ((e, n), (d, n))

def get_prime(bits):
    while True:
        num = random.getrandbits(bits)
        if is_prime(num):
            return num

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def sign_message(private_key, message):
    hashed_message = int.from_bytes(sha256(message.encode('utf-8')).digest(), byteorder='big') % private_key[1]
    d, n = private_key
    signature = pow(hashed_message, d, n)
    return signature

def verify_signature(public_key, message, signature):
    hashed_message = int.from_bytes(sha256(message.encode('utf-8')).digest(), byteorder='big') % public_key[1]
    e, n = public_key
    hash_from_signature = pow(signature, e, n)
    return hashed_message == hash_from_signature

# Example usage:
message = "Hi"

# Generate key pairs
public_key, private_key = generate_key_pair(32)

print(f"Public Key: {public_key}")
print(f"Private Key: {private_key}")

# Sign the message
signature = sign_message(private_key, message)
print(f"Signature: {signature}")

# Verify the signature
is_valid = verify_signature(public_key, message, signature)
print("Signature verification successful!" if is_valid else "Signature verification failed.")
