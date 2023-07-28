from gcd import gcd

# I separated this implementation from main.py for a specific reason:
# I wanted to emphasize the straightforward implementation while also providing a space for this alternative implementation.
# If you don't want to complicate things, avoid checking out this file and simply focus on the decryption process in main.py.

# Note that CRT (Chinese Remainder Theorem) is a faster method for certain modular arithmetic computations.
# It breaks down complex problems into smaller parts, allowing independent and efficient calculations.
# CRT is advantageous when dealing with coprime divisors, smaller numbers, and reducing large exponentiations.
# It is useful in various algorithms but not universally faster for all cases.
# Its speed improvement depends on the specific problem and implementation.

def decrypt_message_CRT(ciphertext, private_key_info):
    modulus = private_key_info['modulus']
    private_exponent = private_key_info['privateExponent']
    prime1 = private_key_info['prime1']
    prime2 = private_key_info['prime2']
    exponent1 = private_key_info['exponent1']
    exponent2 = private_key_info['exponent2']
    coefficient = private_key_info['coefficient']

    # Use the Chinese Remainder Theorem to compute the decryption

    # Calculate the values of dP and dQ using the provided private exponent and primes.
    # dP is the exponent used to decrypt the ciphertext modulo prime1.
    dP = private_exponent % (prime1 - 1)
    # dQ is the exponent used to decrypt the ciphertext modulo prime2.
    dQ = private_exponent % (prime2 - 1)

    # Calculate the modular inverse of prime2 modulo prime1 using the Extended Euclidean Algorithm.
    _, q_inv, _ = gcd(prime2, prime1)
    # If the modular inverse q_inv is negative, add prime1 to make it positive.
    if q_inv < 0:
        q_inv += prime1

    # Calculate the ciphertext raised to dP and dQ modulo prime1 and prime2, respectively.
    # These are intermediate values in the CRT decryption process.
    m1 = pow(ciphertext, dP, prime1)
    m2 = pow(ciphertext, dQ, prime2)

    # Calculate the Chinese Remainder Theorem result (h) using the modular inverse q_inv.
    # h is used to reconstruct the original decrypted message (decrypted_integer).
    h = (q_inv * (m1 - m2)) % prime1

    # Reconstruct the original decrypted integer (decrypted_integer) using the CRT result (h).
    decrypted_integer = m2 + h * prime2

    # Convert the decrypted integer into a string representation (decrypted_message) by converting each byte into a character.

    # Calculate the number of bits required to represent the decrypted integer.
    num_bits = decrypted_integer.bit_length()

    # Initialize an empty list to store the individual bytes of the decrypted integer.
    decrypted_bytes = []

    # Iterate over the bits of the decrypted integer in chunks of 8 (1 byte) at a time, starting from the most significant bit.
    for i in reversed(range(0, num_bits, 8)):
        # Extract each byte using the bitwise right shift operation 'decrypted_integer >> i',
        # and then apply a bitwise 'AND' operation with '0xFF' (255 in decimal) to retain only the last 8 bits.
        byte_value = (decrypted_integer >> i) & 0xFF
        # Append the extracted byte to the list of decrypted bytes.
        decrypted_bytes.append(byte_value)

    # Join the individual bytes as characters to create the decrypted message string.
    decrypted_message = ''.join(chr(byte) for byte in decrypted_bytes)

    return decrypted_message
