'''Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: ínicio, fim e passo, e realize a contagem.
Seu programa tem que realizar três contagens através da função criada:
A) de 1 até 10, de 1 em 1
B) de 10 até 0, de 2 em 2
C) Uma contagem personalizada'''
from math import sqrt
from time import sleep
def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    if inicio > fim:
        if passo > 0:
            passo = - passo
        print(f'Contagem de {inicio} até {fim} de {-passo} em {-passo}')
        print('~~' * 30)
        for v in range(inicio, fim - 1, passo):
            print(v, end ='')
            sleep(0.5)
            print(' => ', end='')
        print('FIM !')
        print('~~' * 30)
    else:
        if passo < 0:
            passo = - passo
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
        print('~~' * 30)
        for v in range(inicio, fim + 1, passo):
            print(v, end ='')
            sleep(0.5)
            print(' => ', end='')
        print('FIM !')
        print('~~' * 30)

contador(1, 10 , 1)

contador(10, 0, -2)

print('Agora é a sua vez de personalizar a contagem !')
i = int(input('Ínicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
print('-=' * 30)
contador(i, f, p)