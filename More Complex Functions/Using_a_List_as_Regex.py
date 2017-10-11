# These are various ways to use a regex on a list to check an input:

# using a list:

def validate_hello(greetings):
    g = ['hello', 'ciao', 'salut', 'hallo', 'hola', 'ahoj', 'czesc']
    for s in g:
        if s in greetings.lower():
            return True
    return False
    
# using a dict:

import re
def validate_hello(greetings):
    greet = {'hello','ciao','salut','hallo','hola','ahoj','czesc'}
    for g in greet:
        p = re.compile(ur''+g, re.IGNORECASE)
        if re.search(p, greetings):
            return True
    return False
    
# using search:

import re

def validate_hello(greetings):
    return bool(re.search("h[ae]llo|ciao|salut|hola|ahoj|czesc", greetings.lower()))
    
from re import compile, search, I

REGEX = compile(r'hello|ciao|salut|hallo|hola|ahoj|czesc', I)

def validate_hello(greeting):
    return bool(search(REGEX, greeting))
    
# in a line:

def validate_hello(greetings):
    return any(x in greetings.lower() for x in ['hello','ciao','salut','hallo','hola','ahoj','czesc'])
