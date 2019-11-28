# Dada una lista solo retornar los elementos enteros

def only_integers(lst):
    #final_list = [hacer for ... if ...]
    final_list = [int(x) for x in lst if isinstance(x,int)]
    return final_list

lst = [1, 2, 3, "x", "y", 10]

only_integers(lst)

"""
[1,2,3,10]
"""
