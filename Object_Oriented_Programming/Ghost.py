# lets make a ghost ;)

import random

class Ghost(object):
  def __init__(self):
    self.color = random.choice(["white", "yellow", "purple", "red"])
    
 or:
 
from random import choice

class Ghost(object):
  def __init__(self):
    self.color = choice(["white",
                         "yellow",
                         "purple",
                         "red"])
    
# TESTS: Describe Ghost class
# it should have a color attribute that is:
# "white", "yellow", "purple", or "red"
ghosts = []

for i in range(1, 101):
    ghosts.append(Ghost().color)
    
# or:

import random

class Ghost(object):
    def __init__(self):
        self.colors = ['white', 'yellow', 'red', 'purple']
        self.color = random.choice(self.colors)

# it "should sometimes make white ghosts"
Test.expect(ghosts.count("white") >= 1) 

# it "should sometimes make yellow ghosts"
Test.expect(ghosts.count("yellow") >= 1)

# it "should sometimes make purple ghosts"
Test.expect(ghosts.count("purple") >= 1)

# it "should sometimes make red ghosts"
Test.expect(ghosts.count("red") >= 1)
