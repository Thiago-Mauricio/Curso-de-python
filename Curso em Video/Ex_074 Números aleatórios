'''Crie um programa que via gerar cinco números aleatórios e colocar em tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e maior valor que estão na tupla.'''

from random import randint
t = randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100)

print(f'Os números gerados foram: {t}')
ma = 0
me = 0
cont = 0
for c in t:
    cont += 1
    if cont == 1:
        me = c
        ma = c
    else:
        if c > ma:
            ma = c
        if c < me:
            me = c
print(f'Dentre os números gerados, o maior é : {ma}')
print(f'E o menor é : {me}')
    
#modelo professor:
print(f'O maior valor sorteado foi {max(t)}')
print(f'O menor valor sorteado foi {min(t)}')