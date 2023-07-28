import re
import os
import subprocess
from base_component import BaseComponent

class Certificate(BaseComponent):
    def __init__(self, filename, csr_filename, private_key_filename):
        self.filename = filename
        self.csr_filename = csr_filename
        self.private_key_filename = private_key_filename

    def generate_file(self):
        os.system('openssl x509 -req -days 365 -in %s -signkey %s -out %s' % (self.csr_filename, self.private_key_filename, self.filename))

    def get_info(self):
        certificate_output = self.get_openssl_info('openssl x509 -in %s -text -noout' % self.filename)
        return self.parse_info(certificate_output)

    def parse_info(self, data):
        # Extract the modulus data from the input data using regular expression search
        modulus_data = re.search(r'Modulus:\s*(.+?)\s*Exponent', data, re.DOTALL).group(1)
        
        # Extract the exponent data from the input data using regular expression search
        exponent_data = re.search(r'Exponent:\s*(\d+)\s+\(', data).group(1)
        
        # Remove any whitespace or colons from the modulus data
        modulus_cleaned = re.sub(r'\s|:', '', modulus_data)
        
        # Convert the cleaned modulus data from hexadecimal to an integer and store it as 'modulus' in the result dictionary
        # Note: The second argument of int() is the base, and 16 is used here because the modulus is in hexadecimal format
        result = {
            'modulus': int(modulus_cleaned, 16),
            
            # Convert the extracted exponent data from a string to an integer and store it as 'exponent' in the result dictionary
            'exponent': int(exponent_data)
        }
        
        return result
