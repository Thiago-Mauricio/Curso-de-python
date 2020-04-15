class Animal(object):
    def __init__(self):
        print('Animal criado.')

    def quemSouEu(self):
        print('Eu sou uma animal.')

    def comer(self):
        print('Comendo...')


animal = Animal()

print(animal.quemSouEu())
print(animal.comer())

class Cachorro(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('Cachorro criado')

    def quemSouEu(self):
        print('Sou um cachorro')

    def latir(self):
        print('Au au.')

sam = Cachorro()
print(sam)
sam.quemSouEu()