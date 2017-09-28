# Building up to the Fizz_Buzz workout:

def pre_fizz(n):
    array =[]
    for x in range(1,n+1):
        array.append(x)
    return array
    
# or you can just do the following:

def pre_fizz(n):
    #your code here
    return list(range(1, n+1))
    
# or as a list expression:

def pre_fizz(n):
    return [i + 1 for i in range(0, n)]
    
# or weirdly as a while loop:

def pre_fizz(n):
    i = 1
    ls = []
    while i <= n:
        ls.append(i)
        i +=1
    return ls
