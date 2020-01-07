# John and Mary want to travel between a few towns A, B, C ... 
# Mary has on a sheet of paper a list of distances between these towns. ls = [50, 55, 57, 58, 60]. 
# John is tired of driving and he says to Mary that he doesn't want to drive more than t = 174 miles and he will visit only 3 towns.
# Which distances they will choose so that the sum of the distances is the biggest possible to please Mary and John?

"""
Example:

With list ls and 3 towns to visit they can make a choice between: 
[50,55,57],[50,55,58],[50,55,60],[50,57,58],[50,57,60],[50,58,60],[55,57,58],[55,57,60],[55,58,60],[57,58,60].

The sums of distances are then: 
162, 163, 165, 165, 167, 168, 170, 172, 173, 175.

The biggest possible sum taking a limit of 174 into account is then 173 and the distances of the 3 corresponding towns is 
[55, 58, 60].
"""


from itertools import combinations

def choose_best_sum(t, k, ls):
    cmb = [comb for comb in combinations(ls, k)]
    saved = 0
    for i in cmb:
        if sum(i) <= t and sum(i) > saved:
            saved = sum(i)
    return saved if saved != 0 else None

