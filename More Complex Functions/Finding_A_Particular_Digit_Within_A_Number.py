# Tricky one this. Enables you to find the nth digit within a number

# the best way to solve it is by using lstrip - if counting right to left, try and except with an int(str) convesion!:

def find_digit(num, nth):
    num = str(num)
    if nth<=0: return -1
    elif nth> len(num): return 0
    else:
        num = num[::-1]
        return int(num[nth-1])
        
# but it can be done simply using this way:

def find_digit(num, nth):
    num = str(num)
    if nth<=0: return -1
    elif nth> len(num): return 0
    else:
        num = num[::-1]
        return int(num[nth-1])
        
 # or you can use .zfill:
 
 def find_digit(num, nth):
    if nth <= 0:
        return -1
    return int(str(abs(num)).zfill(nth)[-nth])
    
 # or -1*nth
 
 def find_digit(num, nth):
    #your code here
    num_str = str(num)
    if nth < 1:
      return -1
    elif nth > len(num_str):
      return 0
    else:
      return int(num_str[-1*nth])
