print('Digite o comprimento de três retas: ')
r1 = float(input('Reta 1: '))
r2 = float(input('Reta 2: '))
r3 = float(input('Reta 3: '))
r12 = r1+r2
r13 = r1+r3
r23 = r2+r3

if r12 > r3 and r13 > r2 and r23 > r1:
    print('Com o comprimento destas retas é possivél formar um triângulo !')
else:
    print('Com o comprimento destas retas não é possivél formar um triângulo !')