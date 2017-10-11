# say you wanted to replace all Thymine with Uracil in order to convert DNA to RNA:
# You could accomplish this by using .replace as a native method or re.sub:

def DNAtoRNA(dna):
    return dna.replace('T', 'U')
    
# or:

import re

def DNAtoRNA(dna):
  return re.sub('T', 'U', dna)
  
# you could also use maketrans:

from string import maketrans
trans = maketrans('T', 'U')

def DNAtoRNA(dna):
    return dna.translate(trans)
    
# or in python 3: 

def DNAtoRNA(dna):
    return dna.translate(dna.maketrans("T", "U"))
    
# or you can use a list exp and iterate over but this is not as good a way to do it:

def DNAtoRNA(dna):
    return "".join(["U" if c=="T" else c for c in dna])
