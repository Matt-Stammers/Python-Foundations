def alias_gen(f_name, l_name):
    first = FIRST_NAME.get(f_name[0].upper())
    last = SURNAME.get(l_name[0].upper())
    return '{} {}'.format(first, last) if first and last else \
        'Your name must start with a letter from A - Z.'
        
# or:



def alias_gen(fn, ln):
    return FIRST_NAME.get(fn[0].upper()) + ' ' +  SURNAME.get(ln[0].upper()) if fn[0].isalpha() and ln[0].isalpha() else 'Your name must start with a letter from A - Z.'
        
# or:
        
def alias_gen(f_name, l_name):
    try:
      return FIRST_NAME[f_name.upper()[0]]+' '+SURNAME[l_name.upper()[0]]
    except:
      return 'Your name must start with a letter from A - Z.'
      
# or a crazy way to do it!:

def is_valid(name):
        return name[0].isalpha()
        
def assign_capcrunch_name(name, pair):
        if is_valid(name):
                return pair[name[0]]
        else:
                raise ValueError('Invalid name entered')

def format_name(name):
        if len(name) > 0:
                return name.lower()[0].upper()
        else:
                raise ValueError('Empty (or anti-matter composed) name entered')

def alias_gen(f_name, l_name):
        try:
                first_name = assign_capcrunch_name(format_name(f_name), FIRST_NAME)
                last_name = assign_capcrunch_name(format_name(l_name), SURNAME)
                result = first_name + " " + last_name
        except ValueError as e:
                result = "Your name must start with a letter from A - Z."

        return result
