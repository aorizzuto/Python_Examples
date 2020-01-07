

# Convertir numero en suma de multiplos de 10. 3450 = 3000 + 400 + 50

def expanded_form(num):
    n = str(num)
    s = ""
    f = 0
    for i in n:
        if i == '0':
            f+=1
            continue
        if f != 0:
            s += ' + '
        s += str(int(i) * 10**(len(n) - f - 1))
        f +=1
        
    return s
