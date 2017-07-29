# Easy program, the maths is the most difficult part of this: effectively it is 1/3rd of all the individual coordinates.

def bar_triang((xA, yA), (xB, yB), (xC, yC)):
    x0 = round((xA + xB + xC) / 3.0, 4)
    y0 = round((yA + yB + yC) / 3.0, 4)
    return [x0, y0]
    
def bar_triang(pointA, pointB, pointC): # points A, B and C will never be aligned
    return [round((pointA[0] + pointB[0] + pointC[0]) / 3.0, 4), round((pointA[1] + pointB[1] + pointC[1]) / 3.0, 4)]   
    
def bar_triang(pointA, pointB, pointC): 
    a = (pointA[0] + pointB[0] + pointC[0]) / 3.0
    b = (pointA[1] + pointB[1] + pointC[1]) / 3.0
    return [round(a, 4), round(b, 4
    
def bar_triang(*args):
    return map(lambda a: round(sum(a) / 3.0, 4), zip(*args))
