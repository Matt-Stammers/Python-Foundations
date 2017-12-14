# This function will calculate the interest accumulated on an investment minus tax and tell you how many years it will take to reach a target:

def calculate_years(principal, interest, tax, desired):
    years = 0
    while principal < desired:
        gain = principal * interest
        post_tax = gain - (gain * tax)
        principal += post_tax
        years += 1
    return years
    
# this can be simplified to the following in one line:

from math import ceil, log
def calculate_years(principal, interest, tax, desired):
    if principal >= desired: return 0
    return ceil(log(float(desired) / principal, 1 + interest * (1 - tax)))
