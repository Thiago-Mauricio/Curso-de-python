from random import shuffle

class Carta(object):
    
    def __init__(self, valor, naipe):
        self.valor = valor
        self.naipe = naipe

    def __repre__(self):
        return '<%s de %>' % (self.valor, self.naipe)