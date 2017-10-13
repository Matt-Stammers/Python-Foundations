# Formatting URL patterns using python to create new ones involves using urllib:

# What is effectively happening in a URL is certain patterns are being substituted as below:

import re

def generate_link(user):
  user = re.sub(' ','%20', user)
  user = re.sub('\[','%5D', user)
  user = re.sub('\:','%3A', user)
  user = re.sub('\{','%7B', user)
  user = re.sub('\!','%21', user)
  user = re.sub('\@','%40', user)
  user = re.sub('\?','%3F', user)
  user = re.sub('\'','%60', user)
  user = re.sub('\~','%7E', user)
  user = re.sub('\>','%3E', user)
  user = re.sub('\+','%2B', user)
  user = re.sub('\;','%3B', user)
  return 'http://www.codewars.com/users/{}'.format(user)
  
# but this won't work as eventually they will conflict - for instance % will mess up some of the other subs.

from urllib import quote

CODEWARS = 'http://www.codewars.com/users/{}'.format

def generate_link(user):
    return CODEWARS(quote(user))
 
# 
 
import urllib

def generate_link(user):
    return 'http://www.codewars.com/users/' + urllib.quote(user)
 
#

import urllib,urlparse
def generate_link(user):
    print user
    s = "http://www.codewars.com/users/"
    u = urllib.quote(user)
    return urlparse.urljoin(s, u)
