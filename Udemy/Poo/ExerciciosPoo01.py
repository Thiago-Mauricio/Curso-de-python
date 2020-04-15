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
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return ((x2-x1) ** 2 + (y2-y1) ** 2)**0.5
        
    
    def slope(self):
        """Retorna a inclinação da reta:"""
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return (y2 - y1) / (x2 - x1)
        

c1 = (3, 2)
c2 = (8,10)
coordenadas = Line(c1, c2)
print(coordenadas.distance())
print(coordenadas.slope())
