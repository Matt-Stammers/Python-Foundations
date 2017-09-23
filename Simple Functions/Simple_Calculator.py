# Simple Calculator - using operator is the best way to build it:

from operator import add, sub, mul, truediv as div

def calculator(x,y,op):
    wrongFunc=lambda x,y: "unknown value"
    return {'+': add, '-': sub, '*': mul, '/': div}.get(op, wrongFunc)(x,y)
    
# this is the most straightforward way to do it in Python:
    
def calculator(x,y,op):
    if op == '+':
        return x + y
    elif op == '-':
        return x - y
    elif op == '*':
        return x * y
    elif op == '/':
        return x / y
    else:
        return "unknown value"
        
  # this is a nice way to do it:
  
  def calculator(x,y,op):
    if str(op) in '+-*/':
        return eval('{}{}{}'.format(x,op,y))
    return "unknown value"
    
 # or you can use .get()
 
 def calculator(x,y,op):
    return {
        '+': x + y,
        '-': x - y,
        '*': x * y,
        '/': x / y
    }.get(op, 'unknown value')

# there are so many ways to handle the error:

def calculator(x,y,op):
    if not str(x).isdigit() or not str(y).isdigit() or not op in ['+', '-', '*', '/']:
        return "unknown value"
    if op == '+':
        return x + y
    elif op == '-':
        return x - y
    elif op == '*':
        return x * y
    elif op == '/':
        return x / y
