class sample(object):
    pass

x = sample()
print(type(x))

class Dog(object):
    especies='mamífero'

    def __init__(self, raça):
        self.raça = raça
        self.numcaract = len(self.especies)

    def latir(self):
        print('Au Au')



sam = Dog(raça='Lab')

print(type(sam))
print(sam.raça)
print(sam.numcaract)
frank = Dog('Huskie')

sam.latir()

class Circulo(object):
    pi = 3.14

    def __init__(self, raio=1):
        self.raio = raio

    def area(self):
        return self.raio ** 2 * pi

    def defRaio(self, raio):
        self.raio = raio

    def obtemRaio(self):
        return self.raio

c = Circulo(2)
print(c.raio)
c.defRaio(3)
print(c.raio)

d = Circulo(5)