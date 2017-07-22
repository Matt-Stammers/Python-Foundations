# Further experience using regex patterns

import re

def contamination(text, char):
    if text == '' or char == '':
        return ""
    else:
        contaminated_word = re.sub('[!#~@$%&*_+{}|:"<>;,/?=a-zA-Z0-9]', char, text)
        return contaminated_word
        
# or a simple way of doing it

def contamination(text, char):
    return char*len(text)
    
def contamination(text, char):
  string = ""
  for x in range(len(text)):
      string += char
  return string
