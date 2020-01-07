
# Una persona puede caminar 10 minutos hacia el [s,n,e,w]. Verificar que la persona vuelva al punto inicial

def is_valid_walk(walk):
    return walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w') if len(walk)==10 else False

