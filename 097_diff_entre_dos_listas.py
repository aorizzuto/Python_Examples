# Diferencia entre dos listas

def diff(l1,l2):
  return list(set(l1)-set(l2))

list1 = [1, 5, 3, 4, 2, 7, 11, 9]
list2 = [1, 2, 9, 5]
print(sorted(diff(list1,list2)))

"""
[3, 4, 7, 11]
"""
