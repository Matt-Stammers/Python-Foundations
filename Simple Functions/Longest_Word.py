# find the longest word in a sentence and return the length of that word:
# a weak way to do it:

def find_longest(string):
    spl = string.split(" ")
    print(spl)
    lens = [len(x) for x in spl]
    print(lens)
    ascending = sorted(lens)
    print(ascending)
    return ascending[-1]
    
# much better:

def find_longest(strng):
    return max(len(a) for a in strng.split())
    
    # or:
    
def find_longest(string):
    return max(map(len, string.split()))
