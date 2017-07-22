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

# or say you wanted to remove all ! but keep one at the end. The first time I tried to do this I could only think to perform it
# in two steps like so

import re

def remove(s):
    no_ex = re.sub('!','', s)
    return ''.join(no_ex + '!')

# but it can actually be achieved much more simply as follows:

def remove(s):
    return s.replace("!", "") + "!"

# or like this:

def remove(s):
    return '{}!'.format(s.replace('!', ''))


# or with .join and a list expression containing s.split
def remove(s):
    return '%s!' % ''.join([x for x in s.split('!')])

# as you can see there are many different ways to do it

def remove(s):
    new_str = ""
    if len(s) > 0:
        for char in s:
            if char != "!":
                new_str += char
        new_str += "!"
    return new_str

# it can even be done like this without re ( a very simple way )

def remove(s):
    newstr = s.replace("!", "")
    return newstr +'!'
