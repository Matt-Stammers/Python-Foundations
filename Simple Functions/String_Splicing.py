def remove_char(s):
    return s[1 : -1]
    
def remove_char(s):
    return '' if len(s) <= 2 else s[1:-1]
    
# weaker methods
    
def remove_char(s):
    n=len(s)
    new=''
    for i in range(0,n):
        if i==0 or i==n-1:
            continue
        else:
            new+=s[i]
            
    return new
    
def remove_char(s):
    return "".join([a[1:-1] for a in s.split()])
    
def remove_char(s):
    length = len(s)
    new_list = []
    for i, c in enumerate(s):
        if i == 0:
            pass
        elif i == (length - 1):
            pass
        elif i != 0 and i != (length - 1):
             new_list.append(c)
    new_string = ''.join(new_list)
    return new_string
