# Formatting URL patterns using python to create new ones involves using urllib:

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
