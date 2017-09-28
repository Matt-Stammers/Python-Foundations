# Given two points in space return the distance between them: This can be done with tuple unpacking or with math functions like hypot:

from math import hypot

def distance_between_points(a, b):
    return hypot(a.x - b.x, a.y - b.y)
    
# or one can calculate it by squaring the outputs and taking the sqrt:

def distance_between_points(a, b):
    return ((b.x - a.x) ** 2 + (b.y - a.y) ** 2) ** 0.5

import math
def distance_between_points(a, b):
    return math.sqrt((a.x - b.x)**2 + (a.y - b.y)**2)
    
def distance_between_points(a, b):
    return round(sum( (d-c)**2 for c,d in zip((a.x, a.y), (b.x, b.y)))**.5, 6)
    
import math
def distance_between_points(a, b):
    x = (a.x - b.x) ** 2 
    y = (a.y - b.y) ** 2
    distance = math.sqrt(x + y)
    return distance
    
# or it can be accomplished by creating a class object:

from math import sqrt

class Point:
    def __init__(self, a, b):
        self.x = a
        self.y = b

def distance_between_points(a, b):
    aa = (a.x-b.x)**2
    bb = (a.y-b.y)**2
    c = sqrt((aa+bb))
    return round(c,6)
