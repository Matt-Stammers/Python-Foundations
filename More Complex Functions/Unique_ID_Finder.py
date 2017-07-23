# Best to use a while loop.

def next_id(arr):    
    t = 0
    while t in arr:
        t +=1
    return t

def next_id(arr):
    counter = 0
    while counter > -1:
        if counter not in arr:
            return counter
        counter += 1
        
# this would work if you just wanted to increment the id

def next_id(arr):
  id = 0
  for x in sorted(arr): id += x == id
  return id

# or this

def next_id(arr):
    if not len(arr): return 0
    d = set(sorted(arr))
    a = set(range(0, max(d) + 1))
    m = a - d
    if m:
        return min(m)
    else:
        return 0 if 0 not in d else max(d) + 1

# or use a hack like this

def next_id(arr):
    if list(arr).__sizeof__()==0:
        return 0
    else:
        for i in range(0, 100000):
            if list(arr).count(i)==0: return i
            
            # this one is quite clever. the one above is not so much

def next_id(arr):
    if not arr:
        return 0
    return min(i for i in xrange(0, max(arr) + 2) if i not in arr)
        
# there are all sorts of hacks you can do to try and find the numbers missing from an array like:

a[-1]*(a[-1] + a[0]) / 2 - sum(a)
#or
sum(xrange(a[0],a[-1]+1)) - sum(a)

# But they are only useful when you are trying to work out a single missing item in a known otherwise complete array.

# you can use Zip and a for loop

def next_id(arr):
    ids = sorted(arr)
    if not ids or ids[0] > 0:
        return 0
    for x, y in zip(ids, ids[1:]):
        if y - x > 1:
            return x + 1
    return ids[-1] + 1
