# This was my first attempt at stripping off the time from some dates, but it is messy and consists of the wrong component parts.

import re

def shorten_to_date(long_date):
    return re.sub(',\s\w\w\w', '', long_date)
    
# This one is much better but the ** is greedy and can escape too much text if you are not careful.

import re

def shorten_to_date(long_date):
    return re.sub(r'\s*,.*', '', long_date)
    
# or you could use this regex which is cleaner

import re

def shorten_to_date(long_date):
  m = re.match('([^,]*),',long_date)
  return m.group(1)
 
# A simple hack to take the end off a string after a particular character is to do the following after the seperator and only take the first part [0]

def shorten_to_date(long_date):
    return long_date.split(',')[0]
    
# or this way
    
def shorten_to_date(long_date):
    short_date = []
    for i in range(len(long_date)):
        if long_date[i] == ',': return ''.join(short_date)
        else: short_date.append(long_date[i])
