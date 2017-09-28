# Given some parameters these will convert them to milliseconds

def past(h, m, s):
    h = (h * 3600) * 1000
    m = (m * 60) * 1000
    s = s * 1000
    return h + m + s
    
def past(h, m, s):
    return (s + (m + h * 60) * 60) * 1000
    
def past(h, m, s):
    if h != 0: h = h * 3600000
    if m !=0: m = m* 60000
    if s !=0: s = s* 1000
    return s+m+h
