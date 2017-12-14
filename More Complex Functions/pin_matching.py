# Say I wanted to create a program that could validate a PIN number as either 4 or 6 digits. There are several ways to do this:

# one way is the following way using match:

import re
def validate_pin(pin):
    return bool(re.match(r'^(\d{4}|\d{6})$',pin))
    
# or even more efficient:

def validate_pin(pin):
    return len(pin) in (4, 6) and pin.isdigit()
