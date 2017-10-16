def find_slope(points):
    try:
        return str((points[3]-points[1])/(points[2]-points[0]))
    except ZeroDivisionError:
        return "undefined"
        
# or:

def find_slope((x1, y1, x2, y2)):
    try:
        return str((y2 - y1) / (x2 - x1))
    except ZeroDivisionError:
        return "undefined"
        
# or:

def find_slope(points):
    a,b,c,d = points
    return 'undefined' if a == c else str((b - d) / (a - c))
