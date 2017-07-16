# The scenario here is a girl pulling out petals and different responses are gained depending how many petals are pulled.
# It can be answered by using moduleo 

def how_much_i_love_you(nb_petals): #Petal Analyser
    if nb_petals % 6 == 0:
        return "not at all"
    elif (nb_petals + 1) % 6 == 0:
        return "madly"
    elif (nb_petals + 2) % 6 == 0:
        return "passionately"
    elif (nb_petals + 3) % 6 == 0:
        return "a lot"
    elif (nb_petals + 4) % 6 == 0:
        return "a little"
    elif (nb_petals + 5) % 6 == 0:
        return "I love you"

# speedy way to do it

def how_much_i_love_you(nb_petals):
    return ["I love you", "a little", "a lot", "passionately", "madly", "not at all"][nb_petals % 6 - 1]
    
# with a dict

def how_much_i_love_you(nb_petals):
    words = {1: 'I love you', 2: 'a little', 3: 'a lot', 4: 'passionately',
            5: 'madly', 0: 'not at all'}
    return words[nb_petals%6]
    
# with a list

phrases = [
    'I love you',
    'a little',
    'a lot',
    'passionately',
    'madly',
    'not at all',
]

def how_much_i_love_you(n):
    return phrases[(n - 1) % len(phrases)]
    
# another way of doing it by wrote    
    
def how_much_i_love_you(nb_petals):
    n = nb_petals % 6
    if n == 1:
        return "I love you"
    if n == 2:
        return "a little"
    if n == 3:
        return "a lot"
    if n == 4:
        return "passionately"
    if n == 5:
        return "madly"
    if n == 0:
        return "not at all"
