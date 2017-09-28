# simply done by escaping the . in a regex

import re
def replace_dots(str):
    return re.sub(r"\.", "-", str)

# or you can use .replace()

def replace_dots(str_):
    if "." in str_: 
        return str_.replace(".", "-") 
    elif str_ is "":
        return ""
    else: 
        return "no dots"
        
# or you can just do:

def replace_dots(string):
    return string.replace('.', '-')
    
# or a crazy way to do it:

def replace_dots(str):
    arr = []
    for i in str:
        if i == '.':
            arr.append('-')
        else:
            arr.append(i)
    
    b = ('').join(arr)
    
    return b
