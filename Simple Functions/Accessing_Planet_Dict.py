# imagine you need to create a dictionary to access planet names by index: Python makes this really easy with .get():

def get_planet_name(id):
    planets = {
        1: "Mercury",
        2: "Venus",
        3: "Earth",
        4: "Mars",
        5: "Jupiter",
        6: "Saturn",
        7: "Uranus",  
        8: "Neptune"}
    return planets.get(id)
    
# you can also call the key, value pairs instead:

def get_planet_name(id):
    # This doesn't work; Fix it!
    name = {
        1: "Mercury",
        2: "Venus",
        3: "Earth",
        4: "Mars",
        5: "Jupiter",
        6: "Saturn",
        7: "Uranus", 
        8: "Neptune"}
        
    for k, v in name.items():
        if id == k:
            return v
    
# or you can just call it on the dictionary:

def get_planet_name(id):
    return {
        1: "Mercury",
        2: "Venus",
        3: "Earth",
        4: "Mars",
        5: "Jupiter",
        6: "Saturn",
        7: "Uranus",
        8: "Neptune",
    }.get(id, None)
    
# or you can do:

def get_planet_name(id):
    plan = {1:"Mercury", 2:"Venus", 3:"Earth", 4:"Mars", 5:"Jupiter", 6:"Saturn", 7:"Uranus", 8:"Neptune"}
    if id in plan:
        return plan[id]

# or rather than using ints for keys:

def get_planet_name(id):
    # This doesn't work; Fix it!
    name=""
    id="case "+ str(id)
    switch={
        'case 1':  "Mercury",
        'case 2':  "Venus",
        'case 3':  "Earth",
        'case 4':  "Mars",
        'case 5':  "Jupiter",
        'case 6':  "Saturn",
        'case 7':  "Uranus",
        'case 8':  "Neptune"}
    return switch.get(id)

# you could also solve it as a list: (less pythonic)

def get_planet_name(id):
    return ["Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune"][id-1]
    
# or if you wanted to hack the list you could do:

def get_planet_name(id):
    return [0, "Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"][id]
    
# or using .index()

def get_planet_name(id):
    names = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    for name in names:
        if (int(id) - 1) == names.index(name):
            return str(name)
