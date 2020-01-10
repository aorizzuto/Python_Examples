# Evaluar string sin usar "eval()". Ej: '3 + 4 / 2 + 5 * 2 / 5' =7

class Calculator(object):
  def evaluate(self, string):
    s = string.split()

    i = 0
    length = len(s)
    
    while i < length:
        if s[i] == '*':
            s[i-1] = str(float(s[i-1]) * float(s[i+1]))
            s.pop(i)
            s.pop(i)
            length = len(s)
            i-=1
        elif s[i] == '/':
            s[i-1] = str(float(s[i-1]) / float(s[i+1]))
            s.pop(i)
            s.pop(i)
            i-=1
            length = len(s)
        elif s[i] == '-':
            s[i+1] = str(int(s[i+1])*(-1))
            s.pop(i)
            i-=1
            length = len(s)
        elif s[i] == '+':
            s.pop(i)
            length = len(s)
        i+=1
    
        
    return sum([int(i) if i.isdigit() else float(i) for i in s])
