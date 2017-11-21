# Say you wanted to create a dictionary of pairs to switch around DNA strands:

pairs = {'A':'T','T':'A','C':'G','G':'C'}
def DNA_strand(dna):
    return ''.join([pairs[x] for x in dna])
    
# or:

def DNA_strand(dna):
    reference = { "A":"T",
                  "T":"A",
                  "C":"G",
                  "G":"C"
                  }
    return "".join([reference[x] for x in dna])
    
# or you could use maketrans:

def DNA_strand(dna):
    return dna.translate(str.maketrans("ATCG","TAGC"))

