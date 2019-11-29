# Write a Python program to get all strobogrammatic numbers that are of length n. Go to the editor
# A strobogrammatic number is a number whose numeral is rotationally symmetric, so that it appears the same when rotated 180 degrees. In other words, the numeral looks the same right-side up and upside down (e.g., 69, 96, 1001).
# For example, Given n = 2, return ["11", "69", "88", "96"]

def reemplazar_por_dicc(i_str,dicc):
    new_str=""
    
    for i in i_str:
        new_str=new_str+str(dicc.get(int(i)))
    
    return new_str[::-1]

def buscar_strobogramatic(num):
    
    dicc={0:0,1:1,6:9,8:8,9:6}
    
    for i in range(10**(num-1),10**num):
        a = i
        i_str=str(i)
        
        new_str = reemplazar_por_dicc(i_str, dicc)
        
        if i_str == new_str:
            print(i, end=" ")
        

def Ejercicio():
    
    buscar_strobogramatic(2)
    print("")
    buscar_strobogramatic(3)
    print("")
    buscar_strobogramatic(4)
        
def main(): 
    Ejercicio() 

# Main function 
if __name__=="__main__":       
    main()

"""
11 69 88 96 
101 111 181 609 619 689 808 818 888 906 916 986 
1001 1111 1691 1881 1961 6009 6119 6699 6889 6969 8008 8118 8698 8888 8968 9006 9116 9696 9886 9966 
"""
