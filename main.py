import re
import os
import subprocess

from private_key import PrivateKey
from csr import CSR
from certificate import Certificate

from ChineseRemainderTheorem.decrypt_message import decrypt_message_CRT

def encrypt_message(message, public_key_info):
    modulus = public_key_info['modulus']
    publicExponent = public_key_info['exponent']

    # Convert the input message to an integer representation (hexadecimal to integer)
    # For each character 'c' in the message, 'ord(c)' returns the ASCII value of 'c'.
    # '{:02x}'.format(ord(c)) formats the ASCII value as a two-digit lowercase hexadecimal representation.
    # This process is done for each character in the message, and all hexadecimal characters are concatenated into a single string.
    # Finally, 'int(..., 16)' converts the concatenated hexadecimal string into an integer.
    message_integer = int(''.join('{:02x}'.format(ord(c)) for c in message), 16)

    # Encrypt the message using RSA encryption (ciphertext = (message_integer ^ publicExponent) % modulus)
    # The 'pow()' function performs the RSA encryption using the public key components.
    # 'message_integer': The integer representation of the input message obtained from the previous step.
    # 'publicExponent': The public exponent of the RSA public key used for encryption.
    # 'modulus': The RSA modulus, another part of the public key.
    # The result of this operation is the encrypted ciphertext.
    ciphertext = pow(message_integer, publicExponent, modulus)

    return ciphertext


def decrypt_message(ciphertext, private_key_info):
    modulus = private_key_info['modulus']
    privateExponent = private_key_info['privateExponent']

    # Decrypt the ciphertext using RSA decryption
    # Perform modular exponentiation to obtain the decrypted integer.
    # The ciphertext is raised to the power of the private exponent modulo the modulus.
    # This results in the decrypted integer representation of the original plaintext message.
    decrypted_integer = pow(ciphertext, privateExponent, modulus)

    # Convert the decrypted integer into a string representation by converting each byte into a character.
    # This involves a bitwise operation to extract each byte (8 bits) of the decrypted integer in reverse order.

    # The 'decrypted_integer.bit_length()' gives the number of bits required to represent the decrypted integer.
    num_bits = decrypted_integer.bit_length()

    # Initialize an empty list to store the individual bytes of the decrypted integer.
    decrypted_bytes = []

    # Iterate over the bits of the decrypted integer in chunks of 8 (1 byte) at a time, starting from the most significant bit.
    for i in reversed(range(0, num_bits, 8)):
        # Extract each byte using the bitwise right shift operation 'decrypted_integer >> i',
        # and then apply a bitwise 'AND' operation with '0xFF' (255 in decimal) to retain only the last 8 bits.
        byte_value = (decrypted_integer >> i) & 0xFF
        decrypted_bytes.append(byte_value)

    # Join the individual bytes as characters to create the decrypted message string.
    decrypted_message = ''.join(chr(byte) for byte in decrypted_bytes)

    return decrypted_message


PRIVATE_KEY = 'key.pem'
CSR_KEY = 'csr.pem'
CERTIFICATE_KEY = 'cert.pem'

key = PrivateKey(PRIVATE_KEY)
csr = CSR(CSR_KEY, PRIVATE_KEY)
certificate = Certificate(CERTIFICATE_KEY, CSR_KEY, PRIVATE_KEY)

# !IMPORTANT!
# The following function is used in scenarios where you do not possess a private key, CSR key, and certificate.
# This function will automatically generate all three components on your behalf.
# key.generate_file()
# csr.generate_file()
# certificate.generate_file()

private_key_info = key.get_info()
csr_info = csr.get_info()
get_key_csr_certificate_info = certificate.get_info()

message = 'Moshe Binieli'
ciphertext = encrypt_message(message, csr_info)
decrypted_message = decrypt_message(ciphertext, private_key_info)
decrypted_message_CRT = decrypt_message_CRT(ciphertext, private_key_info)

print('Original Message:', message)
print('Encrypted Ciphertext:', ciphertext)
print('Decrypted Message:', decrypted_message)
print('Decrypted Message CRT:', decrypted_message_CRT)
