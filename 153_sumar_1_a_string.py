# adicionar 1 al string "hola002" --> "hola003"				

import re

def increment_string(s):
    lst = list(mysplit(s))      # Split string in text + digits
    length = len(lst[-1])       # Save the digit original length
    if length != 0:
        n = str(int(lst[-1])+1) # Add 1
        num = n.zfill(length)   # Fill original length with zeros
        lst.pop()               # Remove original number
        lst.append(num)         # Append new number (original + 1)
    else:
        lst.append('1')         # If there is no number, then add 1
    
    return ''.join(lst)
    
def mysplit(s):
    h = s.rstrip('0123456789')
    t = s[len(h):]
    return h, t
