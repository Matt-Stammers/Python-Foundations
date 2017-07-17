# Tricky one on the surface, but it can easily be accomplished with Python

import datetime
def period_is_late(last,today,cycle_length):
    end_date = last + datetime.timedelta(days=cycle_length)
    return False if end_date>=today else True
    
# there is also a method.days which also uses the timedelta
    
def period_is_late(last,today,cycle_length):
    if (today - last).days > cycle_length:
    	return True
    else:
    	return False

def period_is_late(last, today, cycle_length): # this is the same but neater
    return (today - last).days > cycle_length
    
# or

def period_is_late(last,today,cycle_length):
    return cycle_length < (today - last).days
    
# or calculating the seconds using date!

from datetime import date
def period_is_late(last, today, cycle_length):
    timedelta = today - last
    timedelta_int = timedelta.total_seconds()
    cycle_length_sec = cycle_length * 86400
    return timedelta_int > cycle_length_sec
