# This is for a bucket which might contain gold (a list), if there is gold in the bucket it will return True.

def check_the_bucket(bucket):
    if "gold" in bucket:
        return True
    else:
        return False
        
# or amazingly the following works:

def check_the_bucket(bucket):
    return 'gold' in bucket
    
# really nicely written out.

def check_the_bucket(bucket):
    if 'gold' in bucket:
        print("I will bye a teeth")
        return True
    else:
        print("Not Today")
        return False
        
check_the_bucket(['stone', 'stone', 'gold', 'stone', 'stone'])
check_the_bucket(['stone', 'stone', 'stone', 'stone', 'stone'])
check_the_bucket(['gold', 'gold', 'gold', 'gold', 'gold'])

# you can also compress the list into a set and check that, this saves on memory:

def check_the_bucket(bucket):
    return 'gold' in set(bucket)
