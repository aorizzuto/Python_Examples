def reverse_case(txt):
    s=""
    for i in range(len(txt)):
        if txt[i].islower():
            s = s+txt[i].upper()
        else:
            s = s+txt[i].lower()
    return s

texto = reverse_case("ALEjAndrO")


print(texto)

"""
aleJaNDRo
"""
