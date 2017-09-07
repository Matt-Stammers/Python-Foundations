# simples:

def bmi(weight, height):
    index = weight/(height**2)
    if index <= 18.5:
    	return "Underweight"
    elif index <= 25.0:
    	return "Normal"
    elif index <= 30.0:
    	return "Overweight"
    else:
    	return "Obese"
      
# or

def bmi(weight, height):
    bmi = weight / height ** 2
    return 'Underweight' if bmi <= 18.5 else 'Normal' if bmi <= 25.0 else 'Overweight' if bmi <= 30.0 else "Obese"
    
# or
    
def bmi(weight, height):
    #your code here
    bmi = (weight / (height**2))
    
    if bmi <= 18.5 :
        return "Underweight"
    
    elif bmi > 18.5 and bmi <= 25.0:
        return "Normal"
    
    elif bmi > 25 and bmi <=30.0:
        return "Overweight"
        
    else:
        return "Obese"
