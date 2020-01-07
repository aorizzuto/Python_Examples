
# Descomponer numero en factores primos
def primeFactors(n):
    cont = 2
    lst = []    # List of factors
    
    while n != 1:               # Finish when n = 1
        if n % cont == 0:
            n /= cont        
            lst.append(cont)    # Add factor to list if n is divisible
        else:
            cont += 1
    
    d = {x:lst.count(x) for x in lst}    # Create dictionary with number of times each factor exist
    
    s=""
    for i in sorted(d):
        if d[i]!=1: 
            s += '('+ str(i) + '**' + str(d[i]) + ')'
        else:
            s += '('+ str(i) + ')'
    
    return s
