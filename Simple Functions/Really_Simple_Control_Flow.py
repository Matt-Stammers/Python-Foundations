# This is the code that can be used to check if a character is alive during a game for instance:

def checkAlive(health):
    if health <= 0:
        return False
    else:
        return True
        
# it can be rewritten as:

def checkAlive(health):
    if health > 0:
        return True
    else:
        return False
        
# simple right? - ok check this out:

def checkAlive(health):
    return health > 0
    
# woah, how much better is that!!! mind = blown ;)
