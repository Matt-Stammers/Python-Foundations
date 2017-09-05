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
        
# Here is a very simple example of inheritance - Man() and Woman() both inherit from Human() - they inherit nothing in this case, but if there was anything to inherit they would inherit it.

def God():
    return [Man(), Woman()]

class Human(object):
    pass

class Man(Human):
    pass
    
class Woman(Human):
    pass

# Ok now let's try a fictional Pirate Ship - Ahoy!!!
# This one will board the ship if the ship is more than 20 units cargo than crew. It assumes that crew weigh 1.5 units each.

class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew
        
    def is_worth_it(self):
        self.cargo = self.draft - self.crew * 1.5
        if self.cargo > 20:
            return True
        else:
            return False

# you could then add a rankUp feature to the game to make it more interesting say if more than a certain amount of points are gained.

class player:
    def __init__(self):
        self.rank = 0
    
def playerRankUp(pts):
    try:
        plr()
    except:
        plr = player()
    plr.rank += pts
    return "Well done! You have advanced to the qualifying stage. Win 2 out of your next 3 games to rank up." if plr.rank>99 else False
