# This is a classic puzzle with many variations. Can you return the value of a pair of numbers and work out whether the numbers are both even, or both odd.
# The puzzle is normally expressed as something like two people want to see if they are in love with flowers. Find out if they are (in order for them to be in love they need to not match - Ie. one flower has 4 petals the other 3 or whatever.

def lovefunc( flower1, flower2 ): # this is a basic way of writing this out
    combined = flower1 + flower2
    if combined % 2 == 0:
        return False
    else:
        return True
        
def lovefunc( flower1, flower2 ): # this is a very quick and smart way to do it because moduleo 2 of an even number will always be 0.
    return (flower1+flower2)%2
    
def lovefunc(flower1, flower2): # very similar but not quite as neat
    return flower1 % 2 != flower2 % 2
    
def lovefunc( flower1, flower2 ): # odd's come out at 1 which is obviously the bool for true.
    return (flower1 + flower2) % 2 == 1
    
def lovefunc(a, b): # this is a less good way to solve it
    if a % 2 == 0 and b % 2 == 0:
        return False
    elif a % 2 != 0 and b % 2 == 0:
        return True
    elif a % 2 == 0 and b % 2 != 0:
        return True
    else:
        return False
