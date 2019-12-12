# Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string

first=2
last=2

def sub_str(s):
    return s[:first]+s[len(s)-last:]

# MAIN
s = "Alejandro"
print(sub_str(s))

"""
Alro
"""
