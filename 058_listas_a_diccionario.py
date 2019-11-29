# Write a Python program to print a long text, convert the string to a list and print all the words and their frequencies

string = """Esta es una cadena de texto larga donde se repetiran varias palabras para poder calcular la frecuencia 
de cada una. Esta es la prueba numero 60 aprox de los ejemplos que estoy realizando. La cadena de texto esta en español"""

s = string.split()
rep = [s.count(n) for n in s]

dicc = dict(zip(s, rep))

print(dicc)

"""
{'Esta': 2, 'es': 2, 'una': 1, 'cadena': 2, 'de': 4, 'texto': 2, 'larga': 1, 'donde': 1, 'se': 1, 'repetiran': 1, 'varias': 1, 'palabras': 1, 'para': 1, 'poder': 1, 'calcular': 1, 'la': 2, 'frecuencia': 1, 'cada': 1, 'una.': 1, 'prueba': 1, 'numero': 1, '60': 1, 'aprox': 1, 'los': 1, 'ejemplos': 1, 'que': 1, 'estoy': 1, 'realizando.': 1, 'La': 1, 'esta': 1, 'en': 1, 'español': 1}
"""
