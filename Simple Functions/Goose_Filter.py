# Given some geese can you filter them out of a given list?

geese = {"African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"}

def goose_filter(birds):
    return [bird for bird in birds if bird not in geese]
    
# easy. A list expression is more efficient and easy to fit on a single line.

# however this way might possibly be even quicker:

geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
def goose_filter(birds):
    return list(filter(lambda x: x not in geese, birds))
