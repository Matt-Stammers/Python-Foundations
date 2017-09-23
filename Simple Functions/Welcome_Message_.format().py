# simple welcoming message:

def say_hello(name, city, state):
    return "Hello, {}! Welcome to {}, {}!".format(" ".join(name), city, state)
    
# or not using .format()

def say_hello(name, city, state):
    return 'Hello, ' + ' '.join(name) + '! Welcome to ' + city + ', ' + state + '!'
    
# or

def say_hello(name, city, state):
    greeting = "Hello, {name}! Welcome to {city}, {state}!".format(
        name=" ".join(name),
        city=city,
        state=state
    )
    
    return greeting
    
# or using string selection

def say_hello(name, city, state):
    if len(name) == 2:
       return "Hello, "+name[0]+" "+name[1]+"! Welcome to "+city+", "+state+"!"
    if len(name) == 3:
        return "Hello, "+name[0]+" "+name[1]+" "+name[2]+"! Welcome to "+city+", "+state+"!"
    if len(name) == 4:
        return "Hello, "+name[0]+" "+name[1]+" "+name[2]+" "+name[3]+"! Welcome to "+city+", "+state+"!"
