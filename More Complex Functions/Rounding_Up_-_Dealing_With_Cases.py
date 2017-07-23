import math

def calculate_tip(amount, rating):
    rating = str.lower(rating)
    if rating == 'excellent':
        return int(Decimal(0.20 * amount).quantize(Decimal('1.', rounding=ROUND_UP)))
    elif rating == 'great':
        return int(Decimal(0.15 * amount).quantize(Decimal('1.', rounding=ROUND_UP)))
    elif rating == 'good':
        return int(Decimal(0.10 * amount).quantize(Decimal('1.', rounding=ROUND_UP)))
    elif rating == 'poor':
        return int(Decimal(0.05 * amount).quantize(Decimal('1.', rounding=ROUND_UP)))
    elif rating == 'terrible':
        return int(0 * amount)
    else:
        return 'Rating not recognised'

# This is the best way to solve it.

import math

def calculate_tip(amount, rating):
    rating = str.lower(rating)
    if rating == 'excellent':
        return math.ceil(0.20 * amount)
    elif rating == 'great':
        return math.ceil(0.15 * amount)
    elif rating == 'good':
        return math.ceil(0.10 * amount)
    elif rating == 'poor':
        return math.ceil(0.05 * amount)
    elif rating == 'terrible':
        return math.ceil(0 * amount)
    else:
        return 'Rating not recognised'
        
# This is a hacky way to do it that doesn't work but in a simple problem might solve it, but in general you should use math.ceil.

def calculate_tip(amount, rating):
    rating = str.lower(rating)
    if rating == 'excellent':
        return int(0.20 * amount + 0.5)
    elif rating == 'great':
        return int(0.15 * amount + 0.5)
    elif rating == 'good':
        return int(0.10 * amount + 0.5)
    elif rating == 'poor':
        return int(0.05 * amount + 0.5)
    elif rating == 'terrible':
        return int(0 * amount)
    else:
        return 'Rating not recognised'
        
# This is an even nicer way to solve it.        
        
from math import ceil
def calculate_tip(amount, rating):
    tips = {
        'terrible': 0,
        'poor' : .05,
        'good' : .1,
        'great' : .15,
        'excellent' : .2
    }
    if rating.lower() in tips:
        return ceil(amount * tips[rating.lower()])
        
    else:
        return 'Rating not recognised'
       
# or
import math

def calculate_tip(amount, rating):
    tip_table = {'terrible'     : 0,
                 'poor'         : 0.05,
                 'good'         : 0.10,
                 'great'        : 0.15,
                 'excellent'    : 0.20}
    rating = rating.lower()
    if rating in tip_table:
        return math.ceil(amount * tip_table[rating.lower()])
    else:
        return "Rating not recognised"
        
# or as a list
      
import math
def calculate_tip(amount, rating):
    tipTypes = ["terrible","poor","good","great","excellent"]
    if rating.lower() in tipTypes:
        return math.ceil(amount * tipTypes.index(rating.lower())*0.05)
    else: return "Rating not recognised"
