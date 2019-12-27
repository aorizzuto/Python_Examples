# Verifica prefijo y sufijo
def is_prefix(w, p):
    return p[:len(p)] == w[:len(p)]

def is_suffix(w, s):
    return s[:len(s)] == w[len(w)-len(s):]

print(is_prefix("Alejandro","Ale"))
print(is_prefix("Sebastian","Seva"))
print(is_suffix("Luciano","iano"))
print(is_suffix("Celeste","feste"))

"""
True
False
True
False
"""
