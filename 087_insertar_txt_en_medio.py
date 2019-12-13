# Write a Python function to insert a string in the middle of a string.

def insertar_en_medio(tag,out):
    return tag[:len(tag)//2] + out + tag[len(tag)//2:]

print(insertar_en_medio("{{}}","Alejandro"))
print(insertar_en_medio("[[[]]]","Omar"))
print(insertar_en_medio("<<<<<>>>>>","Rizzuto"))

"""
{{Alejandro}}
[[[Omar]]]
<<<<<Rizzuto>>>>>
"""
