# this code will authenticate santa's sleigh in a simple manner:

class Sleigh(object):
    def authenticate(self, name, password):
        self.name = name
        self.password = password
        if name == 'Santa Claus' and password == 'Ho Ho Ho!':
            return True
        else:
            return False
            
# however, if you wanted to use a hash you could do the following:

class Sleigh(object):
    def __init__(self):
        self.salt = "39d1656331274e45aed30343739ef89b"
        self.enc_password = "45f44255f8b7ac2804a5e008812381297829f64421b69de9c5df0bdc492dab30660ddc67bd3a7cb4c0f3b91eca229131c72abaedb54d8716dc32160d06725879"
        self.username = "Santa Claus"
    def authenticate(self, name, password):
        return name == self.username and hashlib.sha512(password + self.salt).hexdigest() == self.enc_password 
        
# you could also use a dictionary and key:

class Sleigh(object):

    def __init__(self):
        self.known_credentials = {'Santa Claus': 'Ho Ho Ho!'}
        
    def authenticate(self, name, password):
        if name in self.known_credentials.keys() and \
          password == self.known_credentials.get(name):
            return True
        else:
            return False
            
# or using DRY principles:

class Sleigh(object):
    def authenticate(self, name, password):
        return (name, password) == ('Santa Claus', 'Ho Ho Ho!')
        
# or

class Sleigh(object):
    def authenticate(self, name, password):
        return name == 'Santa Claus' and password == 'Ho Ho Ho!'
        
# will do

# as a lambda:

Sleigh = type('Sleigh', (object,), {'authenticate': lambda s, n, p: (n, p) == ('Santa Claus', 'Ho Ho Ho!')})

# or a complex salted-hash!:

import binascii
import hashlib

class Sleigh:
    hashed_passwords = {
        "Santa Claus":
            "sha512:$6$W5MlwJW/JIg6T5e6:1280000:875fee7dec5ba7593e13932e4b16" \
            "a88430807f0b5a61966d30b7fffe157589020b8289f0bad030a6dd1082221be" \
            "8d9adff50b166c0de0e3c6df3f8277250abd2",
    }

    @classmethod
    def authenticate(cls, name, password):
        hashed_password = cls.hashed_passwords.get(name)
        if not hashed_password:
            return False
        algorithm, salt, rounds, hash = hashed_password.split(':')
        return binascii.hexlify(hashlib.pbkdf2_hmac(
            algorithm, password.encode(), salt.encode(), int(rounds)
            )).decode() == hash
