# Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself

s = "alejandro Omar"
letter = "a"
chg = "$"

def new_str(s):
    x = s.replace(letter,chg)
    return s[0]+x[1:]

# MAIN
print("Original:",s)
print("Modificado:",new_str(s))

"""
Original: alejandro Omar
Modificado: alej$ndro Om$r
"""
