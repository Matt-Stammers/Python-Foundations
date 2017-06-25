# Saw you were adding up the price of some medical equipment. You can work out cost vs quantity using a function like this:
def sale_mediquip(n):
    if n < 5:
        return n * 100
    elif n <= 5 or n <10:
        return n * 95
    elif n >= 10:
        return n * 90
        
def sale_mediquip(n):
    return n * (100 if n < 5 else 95 if n < 10 else 90)
