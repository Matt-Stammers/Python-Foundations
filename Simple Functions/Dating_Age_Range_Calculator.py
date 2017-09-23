# this is a simple dating age range calculator - as per the common folklore:

def dating_range(age):
    if age > 14:
        min = int(age/2+7)
        max = int(age-7)*2
        min = str(min)
        max = str(max)
        return "".join(str(min + '-' + max))
    elif age <= 14:
        min = int(age-(0.10*age))
        max = int(age+(0.10*age))
        min = str(min)
        max = str(max)
        return "".join(str(min + '-' + max))
        
# or neater

def dating_range(age):
    if age <= 14:
        min = age - 0.10 * age
        max = age + 0.10 * age
    else:
        min = (age/2)+7
        max = (age-7)*2
        
    return str(int(min))+'-'+str(int(max))
    
# or

def dating_range(age):
    if age < 15:
        return "%d-%d" % (.9*age, 1.1*age)
    else:
        return "%d-%d" % (age/2 + 7, (age - 7) * 2)
        
# or better:

def dating_range(age):
    if age <= 14:
        return "{}-{}".format(int(age-0.1*age), int(age+0.1*age))
    return "{}-{}".format(int(age/2+7), int((age-7)*2))
    
# or in a single line:

def dating_range(age):
    return "{}-{}".format(int(age*0.9),int(age*1.1)) if age<=14 else "{}-{}".format(int(age/2+7),int((age-7)*2))
