# Verificar cantidad de letras diferentes:

def hamming_distance(txt1, txt2):
    cont=0
    for i in range(len(txt1)):
        if txt1[i]!=txt2[i]:
            cont+=1
    return cont

print(hamming_distance("Alejandro","Blejobdri"))

"""
4
"""
