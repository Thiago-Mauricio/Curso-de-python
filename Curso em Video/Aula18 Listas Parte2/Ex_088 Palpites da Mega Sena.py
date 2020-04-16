'''Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo. cadastrando tudo em uma lista composta'''


from random import randint
from time import sleep
print('-' * 40)
print('JOGOS DA MEGA SENA')
print('-' * 40)
jogos = int(input('Quantos jogos você quer que eu sorteie? '))
lista = []
for c in range(0, jogos):
    lista.append([])
    for t in range (0, 6):
        n = randint(1, 60)
        while n in lista[c]:
            n = randint(1, 60)
        lista[c].append(n)
    sleep(1)
    print(f'Jogo {c + 1}: {sorted(lista[c])}')
