'''Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é maior'''
from time import sleep
def maior(* num):
    cont = m = 0
    print('-' * 30)
    print('Os valores recebidos foram: ', end= ' ')
    for c in num:
        cont +=1
        print(c, end=' ')
        sleep (0.5)
        if cont == 1:
            m = c
        else:
            if c > m:
                m = c
    print()
    print('-' * 30)
    print(f'Dentre os valores recebidos o maior foi {m}')
    print('-' * 30)


maior(1, 5, 7, 8, 2, 4)

maior(9, 5, 7, 2, 5)
