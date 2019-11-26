# Write a Python program to concatenate all elements in a list into a string and return it

def concat_str_from_list(lista):
    str=""
    for element in lista:
        str=str+element
    
    return str
        
lista = ['1','2','3','4','5','f','7','a','10']
print("La lista original es:",lista)
print("\nLa lista concatenada es:",concat_str_from_list(lista))

"""
La lista original es: ['1', '2', '3', '4', '5', 'f', '7', 'a', '10']

La lista concatenada es: 12345f7a10
"""
