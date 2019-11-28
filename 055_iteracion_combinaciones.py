# Write a Python program to create all possible strings by using 'a', 'e', 'i', 'o', 'u'. Use the characters exactly once

import itertools

l = ["a","e","i","o","u"]

for L in range(len(l)+1):
    for subset in itertools.combinations(l, L):
        print(''.join(subset))


"""
a
e
i
o
u
ae
ai
ao
au
ei
eo
eu
io
iu
ou
aei
aeo
aeu
aio
aiu
aou
eio
eiu
eou
iou
aeio
aeiu
aeou
aiou
eiou
aeiou
"""
