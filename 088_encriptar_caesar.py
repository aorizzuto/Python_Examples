# Write a Python program to create a Caesar encryption.

def encriptar_caesar(txt,move):
    ret=""
    for i in txt:
        if 65<=ord(i)<=90:
            if ord(i)+move > 90:
                x = ord(i)+move-90+65
            ret=ret+chr(ord(i)+move)
        elif 97<=ord(i)<=122:
            ret=ret+chr(ord(i)+move)
    
    print(ord("a"))
    return ret

print(encriptar_caesar("alejandro",2))
print(encriptar_caesar("z",2))
