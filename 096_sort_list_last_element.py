def last(n): return n[-1]

def sort_list_last(tuples):
  return sorted(tuples, key=last)

lst = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1),(6,6)]
print(sort_list_last(lst))

"""
[(2, 1), (1, 2), (2, 3), (4, 4), (2, 5), (6, 6)]
"""
