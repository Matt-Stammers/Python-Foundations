# Tuple lists. This scenario is to do with people getting on and off a bus in pairs

def number(bus_stops):
    getting_on = sum([pair[0] for pair in bus_stops])
    getting_off = sum([pair[1] for pair in bus_stops])
    print(getting_on)
    print(getting_off)
    return getting_on - getting_off
    
# in one line using a list expression:

def number(bus_stops):
    return sum([stop[0] - stop[1] for stop in bus_stops])
    
# a less readable way which also works
    
def number(stops):
    return sum(i - o for i, o in stops)
    
# as a for loop
    
def number(bus_stops):
    sum=0
    for i in bus_stops:
        sum+=i[0]-i[1]
    return sum
    
# it can also be done using itertools and map:

import operator
import itertools
idx0 = operator.itemgetter(0)
list_of_pairs = [(0, 1), (2, 3), (5, 7), (2, 1)]
sum(itertools.imap(idx0, list_of_pairs)

# and it can be done with zip:

def number(bus_stops):
    num = zip(*bus_stops)
    return sum(num[0])-sum(num[1])

# lambda

def number(bus_stops): return reduce(lambda p, (on, off): p + on - off, bus_stops, 0)
