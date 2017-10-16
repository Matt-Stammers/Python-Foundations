# To localise the barycenter of a triangle:

def bar_triang((xA, yA), (xB, yB), (xC, yC)):
    x0 = round((xA + xB + xC) / 3.0, 4)
    y0 = round((yA + yB + yC) / 3.0, 4)
    return [x0, y0]
    
# or:

def bar_triang(pointA, pointB, pointC): # points A, B and C will never be aligned
    return [round((pointA[0] + pointB[0] + pointC[0]) / 3.0, 4), round((pointA[1] + pointB[1] + pointC[1]) / 3.0, 4)]
    
# or:

def bar_triang(a, b, c):
    return [round(sum(x)/3.0, 4) for x in zip(a, b, c)]
