import re
import os
import subprocess

class BaseComponent():
    def generate_file(self):
        raise NotImplementedError('generate_file() must be implemented by a subclass.')

    def get_openssl_info(self, command):
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()

        if process.returncode == 0:
            return output
        else:
            print('Command execution failed!')
    
    def parse_info(self, data):
        raise NotImplementedError('parse_info() must be implemented by a subclass.')
