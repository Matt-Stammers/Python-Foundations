def next_id(arr):    
    t = 0
    while t in arr:
        t +=1
    return t
    
def next_id(arr):
    if not arr:
        return 0
    return min(i for i in xrange(0, max(arr) + 2) if i not in arr)
    
def next_id(arr):
    counter = 0
    while counter > -1:
        if counter not in arr:
            return counter
        counter += 1
        
# there are all sorts of hacks you can do to try and find the numbers missing from an array like:

a[-1]*(a[-1] + a[0]) / 2 - sum(a)
#or
sum(xrange(a[0],a[-1]+1)) - sum(a)

But they are only useful when you are trying to work out a single missing item in a known otherwise complete array.
