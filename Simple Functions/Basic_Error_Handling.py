# Say you want to specify the inputs to a function such that only ints are accepted:

# This is one way to do it

def int_only(a,b):
  try:
    if type(a) == int and type(b) == int:
      return a%b+b%a
    else:
      return False
  except:
    return False
    
# or you could specify the errors that might result in the except clause: [ this is better ]

def my_first_kata(a, b):
    try:
        return a % b + b % a
    except (TypeError, ZeroDivisionError):
        return False
