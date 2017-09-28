def mult(a, b):
    mv = 0
    for c in range(b):
        mv = sumVal(mv, a)
    return mv

def sumVal(a, b):
    for c in range(b):
        a = add1(a)
    return a
    
def add1(a):
    out = ''
    binval = dec2bin(a)
    carry = 0
    convert = True
    while len(binval) > 0:
        if not convert:
            out = binval[-1] + out
        else:
            if carry == 1:
                if binval[-1] == '0':
                    convert = False
                    carry = 0
                    out = '1' + out
                else:
                    out = '0' + out
            else:
                if binval[-1] == '0':
                    out = '1' + out
                    convert = False
                else:
                    out = '0' + out
                    carry = 1
        binval = binval[:-1]
    if carry == 1:
        out = '1' + out
    return bin2dec(out)
    
def dec2bin(a):
    if a == 0:
        return '0'
    out = ''
    while a > 0:
        out = str(a%2) + out
        a = a //2
    return out

def bin2dec(a):
    out = 0
    while len(a) > 0:
        out *= 2
        out += int(a[0])
        a = a[1:]
    return out
    
def square(n):
    return mult(n,n)
    
# tada, your number is multiplied!
