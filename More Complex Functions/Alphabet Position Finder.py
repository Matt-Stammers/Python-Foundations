def alphabet_position(text): #(super quick way to get the position of a string in a list)
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())