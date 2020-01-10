# De una lista de números y dado un número de indice, indicar cual es el sobreviviente
[1,2,3,4] k=3
[1,2,4]
[1,4]
[1]

def josephus_survivor(n,k):
    lst = list(range(1,n+1))        # List of numbers from 1 to n
    indx = k - 1                    # Start in index = k - 1
    while len(lst)!=1:              # Finish when only 1 element left
        if indx <= len(lst) -1:     # If index lower than length list
            lst.pop(indx)           # Remove item and increase index
            indx = k + indx - 1
        else:
            indx = indx - len(lst)  
    
    return lst[0]                   # Return the only element left
