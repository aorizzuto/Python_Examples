# Obtener la extension
def get_extension(lst):
    return [i.split(".")[1] for i in lst]

print(get_extension(["Alejandro.exe","Omar.txt","Rizzu.xml"]))

"""
['exe', 'txt', 'xml']
"""
