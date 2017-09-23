def list_animals(animals):
    return ''.join('{}. {}\n'.format(i,x) for (i,x) in enumerate(animals, 1))
    
# another way to do it:

def list_animals(animals):
    return "\n".join([str(i+1)+'. '+animal for (i,animal) in enumerate(animals)])+"\n"
    
# animals list

list_animals = lambda a: "".join("{0}. {1}\n".format(i+1, v) for i, v in enumerate(a))

# another way to do it

OUTPUT = '{}. {}\n'.format
def list_animals(animals):
    return ''.join(OUTPUT(i, a) for i, a in enumerate(animals, start=1))
    
# yet another way
    
def list_animals(animals):
    animal_list = []
    for i, animal in enumerate(animals, 1):
        animal_list.append("%d. %s\n" % (i, animal))
    return "".join(animal_list)
