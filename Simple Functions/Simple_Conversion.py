# this function will take in a 'cockroach speed' in km/h and return it in cm/second:

import math

def cockroach_speed(s):
    cm = s * 100000
    sec = (cm / 60) / 60
    return math.floor(sec)
    
    
# this can be neatened as without requiring math:

def cockroach_speed(s):
    cm_per_km = 100000
    sec_per_hour = 3600
    return int(s * cm_per_km / sec_per_hour)
    
# or written out by wrote as:

ONE_KM_IN_METERS = 1000
ONE_METER_IN_CM = 100
ONE_HOUR_IN_MINUTES = 60
ONE_MINUTE_IN_SECONDS = 60

def cockroach_speed(s):
    cm = ONE_KM_IN_METERS * ONE_METER_IN_CM
    sec = ONE_HOUR_IN_MINUTES * ONE_MINUTE_IN_SECONDS
    return int((s * cm) / sec)
    
# or if you want to be a hero you can perform floor division:

def cockroach_speed(s):
    return s // 0.036
