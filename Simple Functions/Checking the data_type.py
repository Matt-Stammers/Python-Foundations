# checking datatypes: this one checks who at the cookie based on the datatype:

# this is the best solution:

def cookie(x):
    return "Who ate the last cookie? It was %s!" % {str:"Zach", float:"Monica", int:"Monica"}.get(type(x), "the dog")
    
# or you can write it out by wrote.

def cookie(x):
    if type(x) == str:
        return "Who ate the last cookie? It was Zach!"
    elif type(x) == bool:
        return "Who ate the last cookie? It was the dog!"
    elif type(x) == int or float:
        return "Who ate the last cookie? It was Monica!"
    else:
        return "Who ate the last cookie? It was the dog!"
        
# you can also solve this by using a dictionary, very pythonic:

def cookie(x):
    try:
        who = {int: 'Monica', float: 'Monica', str: 'Zach'}[type(x)]
    except KeyError:
        who = 'the dog'
    return 'Who ate the last cookie? It was %s!' % who
    
# or using a class method
    
def cookie(x):
    types = {
        'str': 'Zach',
        'int': 'Monica',
        'float': 'Monica'
    }
        
    return 'Who ate the last cookie? It was {0}!'.format(
            types.get(type(x).__name__, 'the dog'))
    
# or you could do it this way:
    
def cookie(x):
    #Good Luck
    if type(x) == type('x'):
        name = "Zach"
    elif type(x) == type(42) or type(x) == type(3.14):
        name = "Monica"
    else:
        name = "the dog"
    return "Who ate the last cookie? It was %s!"%name
