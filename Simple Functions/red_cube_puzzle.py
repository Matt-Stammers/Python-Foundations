''' PROOF:
number of cuts = x
The total number of cubes = (x+1)^3
the number of all blue cubes = (x-1)^3

Number of cubes with one or more red squares:
= (x+1)^3 - (x-1)^3
= (x+1)(x+1)(x+1) - (x-1)(x-1)(x-1)
= x^3 + 3x^2 + 3x + 1 - (x^3 - 3x^2 + 3x -1 )
= 6x^2 + 2
'''

def count_squares(x):
    return 6 * x**2 + 2
    
# or:

def count_squares(x):
    return  (x + 1) ** 3 - (x - 1) ** 3
