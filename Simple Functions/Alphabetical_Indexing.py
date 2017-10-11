# Say you wanted to write a function that given the name of a letter in the alphabet would return that positions letter in a string:

# You could make a dict yourself:

def position(alphabet):
  positions={
    "a":1,
    "b":2,
    "c":3,
    "d":4,
    "e":5,
    "f":6,
    "g":7,
    "h":8,
    "i":9,
    "j":10,
    "k":11,
    "l":12,
    "m":13,
    "n":14,
    "o":15,
    "p":16,
    "q":17,
    "r":18,
    "s":19,
    "t":20,
    "u":21,
    "v":22,
    "w":23,
    "x":24,
    "y":25,
    "z":26
  }
  position = positions[alphabet]
  return "Position of alphabet: {}".format(position)
  
# or:

atoz = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8,
            'i':9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16,
            'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23,
            'x': 24, 'y': 25, 'z': 26}

def position(alphabet):
  return 'Position of alphabet: ' + str(atoz[alphabet])
 
# this works but it is REALLY not necessary:
# you could use list splicing:

def position(alphabet):
    alph_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in range(0, 26):
        if alphabet == alph_list[i]:
            j = i + 1
            return "Position of alphabet: " + str(j)
            
# again this is intuitive but a lot of typing:
# you could abbreviate it by using .find() on the alphabet string like this (even smarter):

def position(alphabet):
    return "Position of alphabet: %s" % ("abcdefghijklmnopqrstuvwxyz".find(alphabet) + 1)
    
# however, even smarter you can use one of the following:

from string import ascii_lowercase
def position(char):
    return "Position of alphabet: {0}".format(
      ascii_lowercase.index(char) + 1)
      
# but the best way has to be using ord:

def position(alphabet):
    return "Position of alphabet: {}".format(ord(alphabet) - 96)
    
# computationally you can't beat that.
