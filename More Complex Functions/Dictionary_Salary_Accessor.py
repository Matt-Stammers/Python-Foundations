# this is a job matching algorithm. This version prints out all the steps as it is working them out the values are stored in a dict.

def match(candidate, job):
    base = candidate['min_salary'] / 100
    print(base)
    close_enough = base * 10
    print(close_enough)
    min_sal = candidate['min_salary'] - close_enough
    print(min_sal)
    if candidate['min_salary'] == None:
        return "Invalid"
    elif min_sal <= int(job['max_salary']):
        return True
    else:
        return False
        
# however a much better way to do it would be this.
        
def match(candidate, job):
    if 'min_salary' in candidate and 'max_salary' in job:
        if (candidate['min_salary'] - (candidate['min_salary'] / 10)) <= job['max_salary']:
            return True
        else:
            return False
    else:
        raise Exception('min_salary or max_salary npot set in candidate or job.')
        
# or a quick hacky way to do it is as follows:

def match(candidate, job):
    return candidate['min_salary'] * 0.9 <= job['max_salary']
    
# or better:

def match(candidate, job):
    if candidate["min_salary"] - candidate["min_salary"] * 0.1 <= job["max_salary"]:
        return True
    else:
        return False
