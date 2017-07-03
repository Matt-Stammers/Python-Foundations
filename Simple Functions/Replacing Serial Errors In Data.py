# These are some various ways you can replace strings with erroneous values when cleaning data (in these examples chaning nubmers back to letters from poor OCR software:

def correct(string): # one method is chaining like this. It's a bit cumbersome though if you have to change a lot of values
    return string.replace('0' , 'O').replace('5', 'S').replace('1', 'I')
    
def correct(string): # this is a simpler way to do it
    return string.translate(str.maketrans("501", "SOI"))
    
tr=str.maketrans('015','OIS')
def correct(string): # or you can split it up like this. This could work well if you don't want your function to become unwieldly
    return string.translate(tr)
    
def correct(string): # you could use a list expression and a dictionary but this is quite unwieldly
    return ''.join({'0':'O', '5':'S', '1':'I'}.get(c, c) for c in string)
 
def correct(string): # again with a list expression except this time specificying that they be digits
    tr = {'0': 'O', '1' : 'I', '5':'S'}
    return ''.join([tr[i] if i.isdigit() else i for i in string])
    
def correct(string): # these are much weaker ways to do it. Try not to do it these ways
    array = list(string)
    another = []
    for i in array:
        if i == '5': another.append('S')
        elif i == '0': another.append('O')
        elif i == '1': another.append('I')
        else: another.append(i)
    return ''.join(another)
    
def correct(s): # second weak method.
    result = ''
    for ch in s:
        if ch == '5':
            result += 'S'
        elif ch == '0':
            result += 'O'
        elif ch == '1':
            result += 'I'
        else:
            result += ch
    return result
