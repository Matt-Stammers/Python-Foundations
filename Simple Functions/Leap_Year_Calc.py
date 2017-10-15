# many ways to do this:

def year_days(year):
  if year % 4 == 0:
    if year % 100 != 0 or year % 400 == 0:
      return str(year) + ' has 366 days'
    else:
      return str(year) + ' has 365 days'   
  else:
    return str(year) + ' has 365 days'
    
# or 
 
from calendar import isleap
def year_days(year):
  return "{} has {} days".format(year, isleap(year) + 365)
  
# or

def year_days(year):
    return '{} has {} days'.format(year, 366 if year % 400 == 0 or (year % 4 == 0 and year % 100) else 365)
    
# or

def year_days(year):
    days = 365
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        days += 1
    return "%d has %d days" % (year, days)
