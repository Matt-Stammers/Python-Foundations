# Say you had a printer that suffered from a particular error rate expressed as any letter outside a-m in a string. How could you report this?

def printer_error(s):
    return "{}/{}".format(len([x for x in s if x not in "abcdefghijklm"]), len(s))
    
# or without the list expression:

from re import sub
def printer_error(s):
    return "{}/{}".format(len(sub("[a-m]",'',s)),len(s))
    
# or it can be done more explicitly using a simple for loop

def printer_error(s):
    errors = 0
    count = len(s)
    for i in s:
        if i > "m":
            errors += 1
    return str(errors) + "/" + str(count)
