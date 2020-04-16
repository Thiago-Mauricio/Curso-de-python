from random import randint
from time import sleep
n = randint(0, 5)
#list = [0, 1, 2, 3, 4, 5]
#n = random.choice(list), usei list na primeira vez que fiz, mas randint é mais eficiente.
print('='*100)
print('Vou pensar em um numero de 0 á 5, tente adivinhar qual...')
print('Pensando...')
#sleep adiciona um temporizador ao programa !
sleep(3)
print('='*100)
m = int(input('Em que número eu pensei? '))
if n == m:
    print('Parabéns, você acertou !!!')
else:
    print(f'Você errou, número que eu pensei foi {n}. \nContinue tentando !!!')
print('='*100)


