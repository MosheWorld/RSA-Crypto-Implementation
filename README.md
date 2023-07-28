# Introduction
## A brief explanation of the RSA algorithm.
RSA (Rivest-Shamir-Adleman) is a widely used encryption and decryption algorithm based on the mathematical properties of large prime numbers. Here's a concise overview of the steps involved:

1. Choose two distinct prime numbers, p and q.
2. Calculate n by multiplying p and q, i.e., n = p * q. This value becomes part of both the public and private keys. (n is called the modulus.)
3. Select an encryption exponent, e, which is a positive integer coprime to (p-1) * (q-1). The public key is now (n, e). (It is noteworthy that the values of e will typically be either 3 or 65537, given that p and q are large)
4. Compute the decryption exponent, d, which is the modular multiplicative inverse of e modulo (p-1) * (q-1). The private key is now (n, d).
5. The public key (n, e) is used for encryption, while the private key (n, d) is used for decryption.

Encryption process:
To encrypt a plaintext message M, the sender uses the recipient's public key (n, e) to compute the ciphertext C as follows: C = M^e (mod n).

Decryption process:
The recipient uses their private key (n, d) to compute the original message M from the ciphertext C: M = C^d (mod n).

The security of RSA is based on the difficulty of factoring the product of two large prime numbers (p and q) and deriving the private key (d) from the public key (n, e) without knowing the prime factors. As long as sufficiently large prime numbers are used, RSA remains secure.
<br><br>
# Example
## Encryption phase: an example using the string "Moshe".
"M" is represented by the ASCII value 77, which is 4d in hexadecimal.<br>
"o" is represented by the ASCII value 111, which is 6f in hexadecimal.<br>
"s" is represented by the ASCII value 115, which is 73 in hexadecimal.<br>
"h" is represented by the ASCII value 104, which is 68 in hexadecimal.<br>
"e" is represented by the ASCII value 101, which is 65 in hexadecimal.<br>
So, when you concatenate the hexadecimal representation of each character in the string "Moshe," you get "4d6f736865" in hex.<br>
Converting it to decimal you get "332582316133".

## Decryption phase: an example using decimal representation generated from the string "Moshe".
Continuing from encryption example of "Moshe that became to "332582316133".
Decimal "332582316133" in binary is "100110101101111011100110110100001100101" (Length 39), therefore num_bits is 39.

### Iteration 0:<br>
**Current i:** 32<br>
**Current decrypted integer:** 332582316133<br>
**Current decrypted integer shifted:** 77<br>
**Current byte value:** 77<br>
**Binary representation of 332582316133:** 100110101101111011100110110100001100101<br>
**Binary representation of 77:** 1001101 (32 bits truncated)

Now, when you perform the bitwise AND operation (77 & 0xFF), you are essentially keeping only the lowest 8 bits of the number.<br>
In binary, 0xFF is represented as 11111111.

**Now let's perform the bitwise AND operation:**<br>
1001101  (77)<br>
&<br>
11111111 (0xFF)<br>
=-------------------=<br>
1001101  (77 in decimal)<br>


### Iteration 1:
**Current i:** 24<br>
**Current decrypted integer:** 332582316133<br>
**Current decrypted integer shifted:** 19823<br>
**Current byte value:** 111<br>


### Iteration 2:
**Current i:** 16<br>
**Current decrypted integer:** 332582316133<br>
**Current decrypted integer shifted:** 5074803<br>
**Current byte value:** 115<br>


### Iteration 3:
**Current i:** 8<br>
**Current decrypted integer:** 332582316133<br>
**Current decrypted integer shifted:** 1299149672<br>
**Current byte value:** 104<br>
**Binary representation of 332582316133:** 100110101101111011100110110100001100101<br>
**Binary representation of 1299149672:** 1001101011011110111001101101000 (8 bits truncated)<br>

Now, when you perform the bitwise AND operation (1299149672 & 0xFF), you are essentially keeping only the lowest 8 bits of the number.<br>
In binary, 0xFF is represented as 11111111.

**Now let's perform the bitwise AND operation:**<br>
1001101011011110111001101101000  (1299149672)<br>
& <br>
11111111 (0xFF)<br>
=-------------------=<br>
1101000  (104 in decimal)<br>


### Iteration 4:
**Current i:** 0<br>
**Current decrypted integer:** 332582316133<br>
**Current decrypted integer shifted:** 332582316133<br>
**Current byte value:** 101<br>

### Result:
The iteration result are: [77, 111, 115, 104, 101] which is "Moshe" in ASCII.