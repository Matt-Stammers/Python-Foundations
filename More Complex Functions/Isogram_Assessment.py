# If you wanted to work out if a string is entirely unique (ie an isogram) there are various ways to do this:
# This is one way to solve it:

def is_isogram(string):
    return True if sorted(string.lower()) == sorted(set(string.lower())) else False
    
# or you can use (even simpler):

def is_isogram(string):
    return len(string) == len(set(string.lower()))
    
# or you can use count and a for loop:

def is_isogram(string):
    string = string.lower()
    for letter in string:
        if string.count(letter) > 1: return False
    return True
