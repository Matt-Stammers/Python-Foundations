# the following will return a string version of the bool:

def boolean_to_string(b):
    return str(b)
    
def boolean_to_string(b):
    return 'True' if b else 'False'
    
def boolean_to_string(b):
    if b:
        return "True"
    return "False"
    
def boolean_to_string(b):
    return ('False', 'True')[b]
    
boolean_to_string = str

boolean_to_string = lambda b : ["False", "True"][b];
