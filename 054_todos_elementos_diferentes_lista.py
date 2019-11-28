# Write a Python function that takes a sequence of numbers and determines if all the numbers are different from each other

def check_list(l):
    l.sort()
    for i in range(len(l)-1):
        if l[i]!=l[i+1]:
            return True
        else:
            return False

l = [1,5,2,7,4,3,8,6,9,1]
l2 = [1,5,2,7,4,3,8,6,9]

print(check_list(l))
print(check_list(l2))

"""
False
True
"""
