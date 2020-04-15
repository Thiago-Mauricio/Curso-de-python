'''Preencha os métodos da classe Line para aceitar coordenadas como um par de tuplas e retornar a inclinação e a distancia da linha'''

from math import sqrt
from math import pow

class Line(object):

    def __init__(self, coor1, coor2):
        """Recebe duas coordenadas cartesiasna."""
        self.coor1 = coor1
        self.coor2 = coor2
        
        
    def distance(self):
        """Calcula a distância entre coor1 e coor2"""
        a = pow((self.coor1[0] - self.coor2[0]), 2)
        b = pow((self.coor1[1] - self.coor2[1]), 2)
        return sqrt(a + b)
        
    
    def slope(self):
        """Retorna a inclinação da reta:"""
        return (self.coor2[1] - self.coor1[1]) / (self.coor2[0] - self.coor1[0])
        

c1 = (3, 2)
c2 = (8,10)
coordenadas = Line(c1, c2)
print(coordenadas.distance())
print(coordenadas.slope())
