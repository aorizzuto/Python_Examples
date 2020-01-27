

# Practica de clases


class auto():
  color = 1
  peso = 100
  marca = 'toyota'

  def set_color(self,c):
    self.color = c
  def set_peso(self,p):
    self.peso = p
  def set_marca(self,m):
    self.marca = m
  def get_color(self):
    return self.color
  def get_peso(self):
    return self.peso
  def get_marca(self):
    return self.marca
    
if __name__ == "__main__":
  
  a = auto()

  print(a.color,a.peso,a.marca)
  a.set_color(2)
  a.set_peso(200)
  a.set_marca('fiat')

  print(a.color,a.peso,a.marca)


"""
1 100 toyota
2 200 fiat
"""

