# Write a Python program to get a list of locally installed Python module

import pkg_resources

def Ejercicio():
    
    installed_packages = pkg_resources.working_set
    installed_packages_list = sorted(["%s      \t=\t%s" % (i.key, i.version)
         for i in installed_packages])
    for m in installed_packages_list:
        print(m)
        
def main(): 
    Ejercicio() 

# Main function 
if __name__=="__main__":       
    main() 
