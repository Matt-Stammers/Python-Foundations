# This will work out how far you are from the number 6.

def six_toast(num):
    rem = 6 - num
    return abs(rem)

# Pos to neg
    
def six_toast(num):
  return abs(num-6)
  
# a less efficient way to solve it:

def six_toast(num):
    if num >= 6:
        t = num-6
        return t
    else:
        return num
        
