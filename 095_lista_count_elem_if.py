# Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings. Go to the editor
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2

def get_items(lst):
    return len([i for i in lst if i[0] == i[len(i)-1] and len(i)>1 ])

lst = ['abc', 'xyz', 'aba', '1221']
print(get_items(lst))

lst = ['abc', 'xyz', 'aba', '1221','23452','a']
print(get_items(lst))

"""
2
3
"""
