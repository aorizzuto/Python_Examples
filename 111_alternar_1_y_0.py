# Se pueden alternar 1 y 0?
def can_alternate(s):
    return abs(s.count("0") - s.count("1"))<=1

print(can_alternate("101001"))
print(can_alternate("100001"))
print(can_alternate("101000011"))
print(can_alternate("1011010111000000"))

"""
True
False
True
False
"""
