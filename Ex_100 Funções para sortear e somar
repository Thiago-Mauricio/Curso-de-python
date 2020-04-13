'''Faça um pograma que tenha um lista chamada números e duas funções chamadas sorteio() e somaPar(). A primeira função vai sortear 5 números e colocálos dentro da lista e a segunda função vai mostrar a soma entre os valores PARES sorteados pela função'''
from random import randint
from time import sleep
def somaPAR(lst):
    soma = 0
    for c in lst:
        if c % 2 == 0:
            soma += c
    print('-=' * 30)
    print(f'Somando os valores pares em {lst}...')
    sleep(2)
    print('-=' * 30)
    print(f'O resulrado foi {soma}')
    print('-=' * 30)

def sorteio():
    valores = []
    print('Sorteando 5 valores para lista...', end=' ')
    sleep(1)
    for valor in range(0, 5):
        valores.append(randint(1, 100))
        print(valores[valor], end=' ')
        sleep(0.5)
    print('PRONTO !')
    somaPAR(valores)


sorteio()
sorteio()
sorteio()
sorteio()
