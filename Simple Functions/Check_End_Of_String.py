# this will check if a letter matches the end of another string, simples:

def correct_tail(body, tail):
    if body.endswith(tail):
        return True
    else:
        return False
        
# or even better:

def correct_tail(body, tail):
    return body.endswith(tail)
    
# or

def correct_tail(body, tail):
    return body[-1] == tail
    
# or

def correct_tail(body, tail):
    return body[-1:] == tail[0]
    
# or

def correct_tail(body, tail):
     sub =[]
     for i in body:
      sub.append(i)
     if sub[-1] == tail:
      return True
     else:
      return False
      
# or

def correct_tail(body, tail):
     sub =[]
     for i in body:
      sub.append(i)
     if sub[-1] == tail:
      return True
     else:
      return False
      
# or

def correct_tail(body, tail):
    sub = body[((len(body)-len(tail))):]
    print sub
    if sub == tail:
        return True
    else:
        return False
