# Write a Python program to print a long text, convert the string to a list and print all the words and their frequencies

def Ejercicio():
    string = """Esta es una cadena de texto larga donde se repetiran varias palabras para poder calcular la frecuencia 
    de cada una. Esta es la prueba numero 60 aprox de los ejemplos que estoy realizando. La cadena de texto esta en español"""

    s = list(string)
    rep = [s.count(n) for n in s]

    dicc = dict(zip(s, rep))

    print(dicc)

def main(): 
    Ejercicio() 

# Main function 
if __name__=="__main__":       
    main() 
    
"""
{'E': 2, 's': 12, 't': 9, 'a': 32, ' ': 43, 'e': 27, 'u': 7, 'n': 10, 'c': 7, 'd': 11, 'x': 3, 'o': 11, 'l': 10, 'r': 13, 'g': 1, 'p': 8, 'i': 4, 'v': 1, 'b': 2, 'f': 1, '\n': 1, '.': 2, 'm': 2, '6': 1, '0': 1, 'j': 1, 'q': 1, 'y': 1, 'z': 1, 'L': 1, 'ñ': 1}
"""
