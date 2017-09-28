def AddExtra(listOfNumbers):
    return listOfNumbers + [1]
    
def AddExtra(listOfNumbers):
    return list(listOfNumbers) + [0]
    
def AddExtra(x):
    res = list(x)
    res.append(0)
    return res
    
def AddExtra(listOfNumbers):
    lst = list()
    for item in listOfNumbers:
        lst.append(item)
        
    lst.append(3)
        
    return lst
