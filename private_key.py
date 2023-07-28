import re
import os
import subprocess
from base_component import BaseComponent

class PrivateKey(BaseComponent):
    def __init__(self, filename):
        self.filename = filename

    def generate_file(self):
        os.system('openssl genrsa -out %s' % self.filename)

    def get_info(self):
        private_key_output = self.get_openssl_info('openssl rsa -in %s -text -noout' % self.filename)
        return self.parse_info(private_key_output)

    def parse_info(self, data):
        # Extract the modulus data from the input data using regular expression search
        modulus_data = re.search(r'modulus:\n\s*(.+?)\n\s*publicExponent', data, re.DOTALL).group(1)
        
        # Extract the public exponent data from the input data using regular expression search
        publicExponent_data = re.search(r'publicExponent:\s*(\d+)', data).group(1)
        
        # Extract the private exponent data from the input data using regular expression search
        privateExponent_data = re.search(r'privateExponent:\n\s*(.+?)\n\s*prime1', data, re.DOTALL).group(1)
        
        # Extract the first prime factor (prime1) data from the input data using regular expression search
        prime1_data = re.search(r'prime1:\n\s*(.+?)\n\s*prime2', data, re.DOTALL).group(1)
        
        # Extract the second prime factor (prime2) data from the input data using regular expression search
        prime2_data = re.search(r'prime2:\n\s*(.+?)\n\s*exponent1', data, re.DOTALL).group(1)
        
        # Extract the first exponent (exponent1) data from the input data using regular expression search
        exponent1_data = re.search(r'exponent1:\n\s*(.+?)\n\s*exponent2', data, re.DOTALL).group(1)
        
        # Extract the second exponent (exponent2) data from the input data using regular expression search
        exponent2_data = re.search(r'exponent2:\n\s*(.+?)\n\s*coefficient', data, re.DOTALL).group(1)
        
        # Extract the coefficient data from the input data using regular expression search
        coefficient_data = re.search(r'coefficient:\n\s*(.+)', data, re.DOTALL).group(1)

        # Remove spaces, newlines, and colons from the extracted data
        modulus_cleaned = re.sub(r'[\s:]', '', modulus_data)
        publicExponent_cleaned = re.sub(r'[\s:]', '', publicExponent_data)
        privateExponent_cleaned = re.sub(r'[\s:]', '', privateExponent_data)
        prime1_cleaned = re.sub(r'[\s:]', '', prime1_data)
        prime2_cleaned = re.sub(r'[\s:]', '', prime2_data)
        exponent1_cleaned = re.sub(r'[\s:]', '', exponent1_data)
        exponent2_cleaned = re.sub(r'[\s:]', '', exponent2_data)
        coefficient_cleaned = re.sub(r'[\s:]', '', coefficient_data)

        # Convert the cleaned modulus, private exponent, prime factors, exponents, and coefficient from hexadecimal to integers
        # Note: The second argument of int() is the base, and 16 is used here because the values are in hexadecimal format
        result = {
            'modulus': int(modulus_cleaned, 16),
            'publicExponent': publicExponent_cleaned,  # Public exponent is kept as a string since it's not in hexadecimal format
            'privateExponent': int(privateExponent_cleaned, 16),
            'prime1': int(prime1_cleaned, 16),
            'prime2': int(prime2_cleaned, 16),
            'exponent1': int(exponent1_cleaned, 16),
            'exponent2': int(exponent2_cleaned, 16),
            'coefficient': int(coefficient_cleaned, 16)
        }
        
        return result
