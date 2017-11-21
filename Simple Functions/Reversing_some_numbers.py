# Number reversal - many ways:

def Descending_Order(num):
    s = str(num)
    s = list(s)
    s = sorted(s)
    s = reversed(s)
    s = ''.join(s)
    return int(s)
    
def Descending_Order(num):
    return int("".join(sorted(str(num), reverse=True)))
    
def Descending_Order(num):
    return int(''.join(sorted(list(str(num)), reverse=True)))
    
Descending_Order = lambda n: int(''.join(reversed(sorted(str(n)))))
