# various ways to use in:

def getCount(inputStr):
    vowels = 'aeiou'
    count = 0
    for x in inputStr:
        if x in vowels:
            count += 1
    return count
        
def getCount(inputStr):
    return sum(1 for let in inputStr if let in "aeiouAEIOU")
    
def getCount(s):
    return sum(c in 'aeiou' for c in s)
    
import re
def getCount(str):
    return len(re.findall('[aeiou]', str, re.IGNORECASE))
    
def getCount(inputStr):
    return sum(inputStr.count(char) for char in ['a', 'e', 'i', 'o', 'u'])
