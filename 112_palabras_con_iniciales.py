# Retornar solo las palabras que empiecen con las iniciales informadas
def dictionary(ini, lst):
    return [i for i in lst if i[:len(ini)]==ini]

print(dictionary("Ale",["Alejandro","Omar","Alero","Alejo","Rizzu","pepino","Alma","Aleman"]))

"""
['Alejandro', 'Alero', 'Alejo', 'Aleman']
"""
