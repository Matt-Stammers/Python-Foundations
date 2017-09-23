# Convert string to float:

def parse_float(string):
    try:
        return float(string)
    except:
        return None
        
# or you can specify the errors:

def parse_float(string):
    try:
        return float(string)
    except (ValueError, TypeError):
        return None
        
# or you can just use pass:

def parse_float(string):
    try:
        return float(string)
    except:
        pass
        
# or a crazy way to do it:

def parse_float(s):
    if type(s) == str and __import__('re').match(r'[\d\.]+', s): return float(s)
    
# if you do want to specify the number only you can use:

def parse_float(string):
    digits = '0123456789'
    dotCount = 0
    for char in string:
        if char == '.':
            dotCount += 1
        elif char not in digits or dotCount > 1:
            return None
    return float(string)
   
# or you can just use isalpha() but again this is comparatively clunky:

def parse_float(string):
  if type(string)==str:
    if string.isalpha():
        return None
    else:
        return float(string)
