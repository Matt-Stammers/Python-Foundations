# Say you wanted to make some dogs who would woof: you could implement the barking method as follows:

class Dog ():
  def __init__(self, breed):
    self.breed = breed
    

snoopy = Dog("Beagle")

snoopy.bark = lambda: "Woof"

scoobydoo = Dog("Great Dane")

scoobydoo.bark = lambda: "Woof"

# or even better:

class Dog ():
  def __init__(self, breed):
    self.breed = breed
    self.bark = lambda: "Woof" # the lambda means you don't need to define a new method outside.
    
snoopy = Dog("Beagle")

scoobydoo = Dog("Great Dane")
