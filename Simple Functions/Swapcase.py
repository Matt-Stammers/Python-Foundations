# Say you wanted to return a bool if two words were exactly opposite cases to one another but in every other way identical.
# You could write out something like this:

def is_opposite(s1,s2):
  letters = []
  if s1 == s2:
    return False
  else:
    for l in s1:
      if l.isupper():
        letters.append(l.lower())
      elif l.islower():
        letters.append(l.upper())
  s1_word = ''.join(letters)
  if s1_word == s2:
    return True
  else:
    return False
    
# This would work, but it is not very efficient. In later versions of python a method .swapcase makes this much easier:

def is_opposite(s1, s2):
    return False if not(s1 or s2) else s1.swapcase() == s2
    
# or slightly more intuitively:

def is_opposite(s1, s2):
    return bool(s1) and s1.swapcase() == s2
    
# more clearly this would look like:

def is_opposite(s1,s2):
  if s1.swapcase() == s2 and s1 != "":
    return True
  else:
    return False

# or you could even zip the lists, but this is moving back into less efficient territory:

def is_opposite(s1,s2):
  # your code here
  if s1 == '' or s2 == '':
      return False
  a1 = list(s1)
  a2 = list(s2)
  z=list(zip(a1,a2))
  for i in range(len(z)):
      if z[i][0] == z[i][1]:
          return False
  return True
