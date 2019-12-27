# Si a=1, b=2...etc, crear funcion que devuelva la suma de estos en un string

def how_many_times(msg):
    return sum([ord(i) - 96 for i in msg])

print(how_many_times("alejandro"))

"""
80
"""
