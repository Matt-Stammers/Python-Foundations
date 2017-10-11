# Returning numbers only: can use isdigit() or r'\D' to sub all non-digits

def get_number_from_string(string):
    return int(''.join(x for x in string if x.isdigit()))
    
def get_number_from_string(string):
    return int("".join([i for i in string if i in "0123456789"]))
    
def get_number_from_string(string):
    a = filter(lambda x:x.isdigit(),list(string))
    s=''.join(list(a))
    return int(s)
    
import re
def get_number_from_string(s):
    return int(re.sub(r'\D', '', s))
    
def get_number_from_string(string):
  return int(__import__('re').sub('\D', '', string))
