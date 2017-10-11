# say you want to reply to an input based on its string values:
# you could specify each argument in turn:

def quote(fighter):
  fighter = fighter.lower()
  if fighter == "george saint pierre":
    return "I am not impressed by your performance."
  else:
    return "I'd like to take this chance to apologize.. To absolutely NOBODY!"
    
# but this gets arduous when there are lots of options:
# instead start a dictionary and then return the dict:

statements = {
    'george saint pierre': "I am not impressed by your performance.",
    'conor mcgregor': "I'd like to take this chance to apologize.. To absolutely NOBODY!"
}

def quote(fighter):
    return statements[fighter.lower()]
    
# simples
