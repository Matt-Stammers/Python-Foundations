# Say you wanted to add the shortest string from a pair to the beginning and end of the other: This could be achieved by:

def solution(a, b):
    if len(a) > len(b):
    	return "".join(b+a+b)
    else:
    	return "".join(a+b+a)
      
# or even better:

def solution(a, b):
    return '{0}{1}{0}'.format(*sorted((a, b), key=len))
    
