# 

def Ejercicio():
    
    dicc = {
    "1": "abc",
    "2": "def",
    "3": "ghi",
    "4": "jkl",
    "5": "mno",
    "6": "pqrs",
    "7": "tuv",
    "8": "wxy",
    "9": "z"
    }
    
    list_keys = [ k for k in dicc ]
    list_values = [ v for v in dicc.values() ]
    list_key_value = [ [k,v] for k, v in dicc.items() ]
    
    print(dicc)
    print(list_keys)
    print(list_values)
    print(list_key_value)
        
def main(): 
    Ejercicio() 

# Main function 
if __name__=="__main__":       
    main() 
    
"""
{'1': 'abc', '2': 'def', '3': 'ghi', '4': 'jkl', '5': 'mno', '6': 'pqrs', '7': 'tuv', '8': 'wxy', '9': 'z'}
['1', '2', '3', '4', '5', '6', '7', '8', '9']
['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxy', 'z']
[['1', 'abc'], ['2', 'def'], ['3', 'ghi'], ['4', 'jkl'], ['5', 'mno'], ['6', 'pqrs'], ['7', 'tuv'], ['8', 'wxy'], ['9', 'z']]
"""
