# what if you want to check if an input is a string. This can be achieved by isinstance():

def repeat_it(string,n):
    return string * n if isinstance(string,str) else 'Not a string'
    
def repeat_it(string,n):
    return string * n if isinstance(string, (str, unicode)) else "Not a string"
    
# or it can be done any of the other ways below:

def repeat_it(string,n):
    if type(string) is not str:
        return 'Not a string'
    return string * n
    
def repeat_it(string,n):
    if type(string) is str:
        return ''.join(string * n)
    else:
        return 'Not a string'
        
def repeat_it(string,n):
    if type(string) is not str:
        return 'Not a string'
    return string * n
