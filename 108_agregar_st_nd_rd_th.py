# Agregar st,nd,rt,th a numeros 1st, 2nd, 3rd, etc
def return_end_of_number(num):
    lst=["-TH","-ST","-ND","-RD"]
    return (str(num)+lst[num%10] if 0 < num%10 < 4 else str(num)+lst[0])

print(return_end_of_number(31))
print(return_end_of_number(52))
print(return_end_of_number(77))
print(return_end_of_number(103))

"""
31-ST
52-ND
77-TH
103-RD
"""
