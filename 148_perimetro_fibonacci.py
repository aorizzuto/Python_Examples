
# Perimetro total de serie fibonacci (cuadrados: 1 1 2 3 5 8 13...)

def perimeter(n):
    return 4*fib(n+1)

def fib(n):
    a = 0
    b = 1
    l=[1]
    if n < 2:
        return n 
    else: 
        for i in range(2,n+1): 
            c = a + b 
            a = b 
            b = c 
            l.append(c)
        return sum(l)
