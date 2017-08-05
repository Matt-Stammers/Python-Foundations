# this is a basic introduction to OOP in Python for medics
# classes are by convention capitalized to seperate them from functions

class Sample():
  pass

x = Sample()

print(type(x))

# this is now a class 'object'
# Ok so now lets make a more intuitive example

class Cat():
  pass

mycat = Cat()

print(type(mycat))

# again it is a class called .Cat
# ok so now we will build the object using __init__ and self

class Cat():
  
  def __init__(self, breed):
    self.breed = breed
    
mycat = Cat(breed = "Tabby")

print(type(mycat))
print(mycat.breed)

# this will print only the attribute - "Tabby" which is an attribute of the cat class
# ok lets just add another attribute

class Cat():
  
  def __init__(self, breed, name):
    self.breed = breed
    self.name = name
    
mycat = Cat(breed = "Tabby", name = "Jonno")

print(type(mycat))
print(mycat.breed)
print(mycat.name)

# viola, the attributes are now printed to the console
# ok so how about class object attributes

class Cat():

  # This is the class object attribute
  kingdom = "animal"
  
  def __init__(self, breed, name):
    self.breed = breed
    self.name = name
    
mycat = Cat(breed = "Tabby", name = "Jonno") # this (mycat) is the instance

print(type(mycat))
print(mycat.breed)
print(mycat.name)
print(mycat.kingdom)

# This will now print out the kingdom animal which is the class attribute
# ok now lets try with methods

class Circle():
  
  pi = 3.14
  
  def __init__(self, radius=2):
    self.radius = radius
    
  def area(self):
    return self.radius*self.radius* Circle.pi
    
mycirc = Circle(3) # mycirc is the 'instance' of circle
print(mycirc.radius)
print(mycirc.pi)

# the answer here was 3 which is the radius plus pi.
# but how do we get the area?

print(mycirc.area())

# this returns the area of 28.26 - .area() must have a () at the end
# but how do we redefine the parameter radius? 2 options:

mycirc.radius = 500
print(mycirc.area())

# or

class Circle():
  
  pi = 3.14
  
  def __init__(self, radius=2):
    self.radius = radius
    
  def area(self):
    return self.radius*self.radius* Circle.pi
    
  def set_radius(self, new_r):
    self.radius = new_r
    
mycirc.set_radius(500)
print(mycirc.area())
