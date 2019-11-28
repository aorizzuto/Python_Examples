def ordenar(txt):
    lista = list(txt)
    lista.sort()
    return "".join(map(str,lista))

texto = ordenar("alejandro")

print(texto)

"""
aadejlnor
"""
