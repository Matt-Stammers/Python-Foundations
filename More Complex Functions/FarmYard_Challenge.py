# Returns the number of cows and chickens in the farm given a number of heads and legs

def animals(heads, legs):
    chickens, cows = 2*heads-legs/2, legs/2-heads
    if chickens < 0 or cows < 0 or not chickens == int(chickens) or not cows == int(cows):
        return "No solutions"
    return chickens, cows
    
# or

def animals(heads, legs):
    chickens = heads * 2 - legs / 2
    cows = heads - chickens
    if chickens < 0 or cows < 0 or chickens != int(chickens):
        return "No solutions"
    return (chickens, cows)
