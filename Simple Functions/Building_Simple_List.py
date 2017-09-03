# This is a really simple challenge. It focusses on how to build up a simple list using a while loop. My first solution was:

def monkey_count(n):
    num_list = []
    y = 0
    while y<n:
        y += 1
    	num_list.append(y)
    return num_list
    
# intuitive and it works, but check this out!

def monkey_count(n):
    return range(1, n+1)
    
# sneaky, also this:

def monkey_count(n):
    return [i+1 for i in range(n)]
    
# or this:

def monkey_count(n):
    return list(range(1,n+1))
    
# or even a lambda:

monkey_count=lambda n: range(1,n+1)
    
# these are much better in terms of neatness
