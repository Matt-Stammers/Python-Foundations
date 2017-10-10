# What if you just wanted to split a word in half and return each half on its own:
# You could do the following:

def reverse(st):
    words = list(st.split(' '))
    print(words)
    rev_word = words[::-1]
    print(rev_word)
    return ' '.join(rev_word)
    
# but this can be condensed to one sentence:

def reverse(st):
    return ' '.join(st.split(' ')[::-1])
    
# or like this:

def reverse(st):
    return ' '.join(reversed(st.split(' ')))
