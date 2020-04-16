'''Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário. No fianl coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado'''
from random import randint
from operator import itemgetter
jogadores = {}
print('-=' * 20)
print('{:^30}'.format('RESULTADO') )
print('-=' * 20)
jogadores['Jogador 1'] = randint(1, 6)
jogadores['jogador 2'] = randint(1, 6)
jogadores['jogador 3'] = randint(1, 6)
jogadores['jogador 4'] = randint(1, 6)
ranking = {}
for k, v in jogadores.items():
    print(f'{k} tirou {v} no dado.')
print('-=' * 20)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for c, v in enumerate(ranking):
    print(f' {c+1}º lugar: {v[0]} com {v[1]}.')
print('-=' * 20)