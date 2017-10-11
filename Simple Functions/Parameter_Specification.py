# Say we wanted to define a function that accepts one argument based on a particular parameter and returns a value based on that parameter.

def howManyLightsabersDoYouOwn(x=""): # Note:that in order to allow the function not to break when it is called empty a parameter must be specified
  try:
    if x == "Zach":
      return 18
    elif x != "Zach":
      return 0
  except:
    return 0
    
test.assert_equals(howManyLightsabersDoYouOwn("Zach"), 18)
test.assert_equals(howManyLightsabersDoYouOwn(), 0)
test.assert_equals(howManyLightsabersDoYouOwn("zach"), 0)

# this works as well:

def howManyLightsabersDoYouOwn(name=""):
    return (18 if name=="Zach" else 0)
