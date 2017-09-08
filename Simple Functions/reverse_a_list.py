# simples

def reverse_list(l):
  return l[::-1]
  
# or

def reverse_list(l):
  """return a list with the reverse order of l"""
  return list(reversed(l))

# or

def reverse_list(l):
  l.reverse()
  return l

# or weirdly

def reverse_list(l):
    if len(l) == 1 : return [l[0]]
    else: return [l[-1]]+reverse_list(l[:-1])

# or

def reverse_list(l):
  return [r for r in reversed(l)]

# or even more weirdly

def reverse_list(l):
    answer = []
    counter = (len(l)-1)
    while counter >= 0:
        answer.append(l[counter])
        counter = counter - 1
    return answer
