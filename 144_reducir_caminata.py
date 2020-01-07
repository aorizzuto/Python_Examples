
# Eliminar pasos de mas: north-south west-east

def dirReduc(arr):
    try:
        lst = [i.upper() for i in arr]
        print(arr)
        done=1
        i=0
        f=0
        
        while done:
            
            if lst[i]=='NORTH' and lst[i+1]=='SOUTH':
                f=1
            elif lst[i]=='SOUTH' and lst[i+1]=='NORTH':
                f=1
            elif lst[i]=='WEST' and lst[i+1]=='EAST':
                f=1
            elif lst[i]=='EAST' and lst[i+1]=='WEST':
                f=1
            if f:
                lst.pop(i+1)
                lst.pop(i)
                i=0
                f=0
            else:
                i+=1
            
            if i+1 >=len(lst):
                break
        return lst
    except:
        return arr
