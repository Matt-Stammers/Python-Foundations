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

# or consider a simple grading system: This can also be collapsed as follows:

def grader(x):
  if 0.9 <= x <= 1: return "A"
  elif 0.8 <= x < 0.9: return "B"
  elif 0.7 <= x < 0.8: return "C"
  elif 0.6 <= x < 0.7: return "D"
  else: return "F"
