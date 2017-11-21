# Extracting middle characters from a string can achieved any number of ways:

# an ugly way to do it:

def get_middle(s):
    i = 0
    for x in s:
        i += 1
    print(i)
    middle = (i/2)
    print(middle)
    if i % 2 == 0:
        return "".join(s[middle-1]+s[middle])
    else:
        return s[middle]
        
# This can be cleverly abbreviated as follows;

def get_middle(s):
   return s[(len(s)-1)/2:len(s)/2+1]
   
# or one can use divmod:

def get_middle(s):
    index, odd = divmod(len(s), 2)
    return s[index] if odd else s[index - 1:index + 1]
    
# or:

def get_middle(s):
    strLen = len(s)
    if(strLen%2==0):#even
        return s[strLen/2-1:strLen/2+1]
    else:#odd
        return s[strLen/2]
