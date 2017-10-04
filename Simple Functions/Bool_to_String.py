# Really simple function here

def bool_to_word(bool):
    if True:
        return "Yes"
    elif False:
        return "No"
    else:
        return "You have made an Error"
        
# or even better

def bool_to_word(bool):
    return "Yes" if bool else "No"
    
def bool_to_word(bool):
    return ['No', 'Yes'][bool]
    
def bool_to_word(bool):
    return bool and "Yes" or "No"
    
def bool_to_word(bool):
    return str(bool)
