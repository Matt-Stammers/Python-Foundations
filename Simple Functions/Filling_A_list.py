# Say you wanted to fill a broken list with the correct values with increments of one. 
# This can be done as follows:

def pipe_fix(x):
  pipe = []
  pipe_start = x[0]
  pipe_finish = x[-1]
  print(pipe_start)
  print(pipe_finish)
  for n in range(pipe_start, pipe_finish+1):
    pipe.append(n)
  return pipe
  
# but this a very cumbersome way to do it.
# Instead you could abbreviate the above to a more data efficient version:

def pipe_fix(arr):
    ls = []
    for i in range(arr[0],arr[len(arr)-1]+1):
        ls.append(i)
    return ls
    
# This can be further condensed into a list expression: Even better!:

def pipe_fix(l):
  return [x for x in range(min(l), max(l)+1)]
  
# This is even more elegant:

def pipe_fix(arr):
  return range(min(arr), max(arr)+1)
