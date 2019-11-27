# Write a Python program to check if a string is numeric

def is_numeric(x):
    ret = True
    try:
        float(x)
    except (ValueError, TypeError):
        ret = False
    
    return ret

################

a = 4
b="h"

print(is_numeric(a))
print(is_numeric(b))

"""
True
False
"""
