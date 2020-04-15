from random import randint
from time import sleep
c = randint(1,10)
soma = 1
print('=' * 100)
print('VOU PENSAR EM UM NÚMERO INTEIRO ENTRE 1 E 10: ')
print('PENSANDO....')
sleep(3)
jogador = int(input('VOCÊ CONSEGUE ADVINAR EM QUAL NÚMERO EU PENSEI? '))
while jogador != c:
    jogador = int(input(('Ainda não foi desta vez, tente denovo: ').upper()))
    soma += 1
    while jogador <1 or jogador > 10:
        jogador = int(input('Não se esqueça que o número está entre 1 e 10, tente denovo:').upper())
if soma == 1:
    print(('Uowwwwwww!!! Você advinhou de primeira parabêns!!!').upper())
elif soma < 3:
    print((f'Parabêns você só precisou de {soma} palpites para acertar !!!').upper())
elif soma < 6:
    print((f'Parabêns você acertou! E precisou de {soma} palpites para acertar').upper())
elif soma <=9:
    print((f'Demorou mais você conseguiu, você precisou de {soma} palpites para acertar').upper())
else:
    print((f'Você acertou, mas depois de chutar todos os números ficou fácil não é mesmo!').upper())
print('=' * 100)