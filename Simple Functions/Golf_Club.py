# This takes in a load of lists and returns the rating of that 

def openOrSenior(data):
    senior = 'Senior'
    open_ob = 'Open'
    output = []
    for item in data:
        if item[0] >= 55 and item[1] > 7:
            output.append(senior)
        else:
            output.append(open_ob)
    return output
   
# must better:

def openOrSenior(data):
    return ["Senior" if age >= 55 and handicap >= 8 else "Open" for (age, handicap) in data]
  
# as a list exp:
  
def openOrSenior(members):
    return ["Senior" if m[0]>54 and m[1]>7 else "Open" for m in members]
    
# another way to express it:

def openOrSenior(data):
    return ["Senior" if age >= 55 and handicap > 7 else "Open" for age, handicap in data]
