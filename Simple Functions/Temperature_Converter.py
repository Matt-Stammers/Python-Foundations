# Converting farenheit to celcius:

def weather_info (temp):
    c = convertToCelsius(temp)
    if (c <= 0):
        return (str(c) + " is freezing temperature")
    else:
        return (str(c) + " is above freezing temperature")
    
def convertToCelsius (temperature):
  celsius = (temperature - 32) * (5.0/9.0)
  return celsius
  
# or much simpler:

def weather_info (temp):
    t = (temp - 32)
    print(t)
    c = t * 0.5555555555556 # alternatively could use 5.0/9.o but must be a float involved in the division.
    print(c)
    if c > 0:
        return "{} is above freezing temperature".format(c)
    else:
        return "{} is freezing temperature".format(c)
        
# or:

def weather_info (t):
  c = (t - 32) * (5.0 /9)
  return str(c) + " is freezing temperature" if c <= 0 else str(c) + " is above freezing temperature"
