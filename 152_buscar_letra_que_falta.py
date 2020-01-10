
# Buscar letra que falta

import string

def find_missing_letter(chars):
    lst = [chr(x) for x in range(ord(chars[0]), ord(chars[len(chars)-1]))]
    return ([i for i in lst if i not in chars][0])
