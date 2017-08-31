# In this scenario you are a book publisher looking for good ideas in an array. If there are >2 good ideas you detect a series and return accordingly

# Note: this is the easy version of this problem. There is a second much more complex version

# this is one way to solve it

def well(x):
  series = 0
  for idea in x:
    if idea == 'good':
      series = series + 1
  if series >=3:
    return 'I smell a series!'
  elif series >=1:
    return 'Publish!'
  else:
    return 'Fail!'
    
# or it can be done using .append():

def well(x):
    l= list()
    for n in x:
        if n=='good':
            l.append(n)
    return 'I smell a series!' if len(l) > 2 else 'Publish!' if len(l) else 'Fail!'
    
# or much more collapsed you can just use .count()

def well(x):
    c = x.count('good')
    return 'I smell a series!' if c > 2 else 'Publish!' if c else 'Fail!'
    
# or in a single line!:

def well(a):c=a.count('good');return['Fail!','Publish!','I smell a series!'][(c>0)+(c>2)]
