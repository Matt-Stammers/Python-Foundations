class Hero(object):
    def __init__(self, name='Hero'):
        self.name = name
        self.position = '00'
        self.health = 100
        self.damage = 5
        self.experience = 0
        
# ok so this is one way to create the hero in a game say with a default attribute set.
# However, this is another way including max_health which is very important if the game is to be at all realistic.

class Hero(object):
    def __init__(self, name="Hero", position="00",
        health=100, damage=5, experience=0):
        self.name = name
        self.position = position
        self.max_health = health 
        self.health = health 
        self.damage = damage
        self.experience = experience
        
# or say you wanted to create a person class and then iterate over that class using different names. You could use the following:

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.info='{}s age is {}'.format(name, age)
        
# You could then use a for loop to iterate over this:

names=["john","matt","alex","cam"]
ages=[16,25,57,39]
for i in range(4):
    name,age=names[i],ages[i]
    person=Person(name,age)
    
# Then you can add more attributes and even inherit from other classes. Consider this cat example which has inherited from the animal class:

class Cat(Animal):
    def __init__(self, name):
        self.name = name
    def speak(self):
        return '{} meows.'.format(self.name)
        


