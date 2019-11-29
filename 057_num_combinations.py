# Write a Python program to find unique triplets whose three elements gives the sum of zero from an array of n integers

import itertools

x = [-6,2,8,1,-1,4,0]
find = 0
cant_numbers = 3

result = []

for i in range(len(x),0,-1):
    for seq in itertools.combinations(x,i):
        if sum(seq) == find and len(seq)==cant_numbers:
            result.append(seq)

# Otra forma:
# result = [seq for i in range(len(x), 0, -1) for seq in itertools.combinations(x, i) if sum(seq) == find and len(seq)==cant_numbers]

print(result)

"""
[(-6, 2, 4), (1, -1, 0)]
"""
