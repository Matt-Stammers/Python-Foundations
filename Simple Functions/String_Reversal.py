# many ways to reverse a string. In python it is not difficult:

def solution(s):
    return s[::-1]
    
# another way
    
def solution(string):
    letters = list(string)
    letters.reverse()
    return "".join(letters)
    
def solution(string):
    r =""
    for i in reversed(string):
        r += i
    return r
    
# a slightly mad way:
    
def solution(string):
    return ''.join(list(reversed(list(string))))
    
# a crazy way to do it.

def solution(string):
    list = []
    for i in range(0, len(string)):
        list.append(string[i])
    list_2=list[::-1]
    return ''.join(list_2)
