# Taking a list and turning it into a string can be achieved with:

def smash(words):
    return ' '.join(i for i in words)
    
# or just: 

def smash(words):
    return " ".join(words)
    
# or:

def smash(words):
    new_words = ""
    for word in words:
        if len(new_words) == 0:
            new_words += word
        
        else:
            new_words = new_words + " " + word 
        
    return new_words
    
# but this is pretty verbose and certainly inferior.
