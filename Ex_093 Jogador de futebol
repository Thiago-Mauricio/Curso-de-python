'''Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato'''
jogador = {}
gols = []
print('=-' * 30)
jogador['nome'] = input('Nome do jogador: ')
jogador['partidas'] = int(input('Quantidade de partidas jogadas: '))
print('=-' * 30)
for c in range(0, jogador['partidas']):
    gols.append(int(input(f'Gols na {c + 1}ª partida: ')))
jogador['gols'] = gols
jogador['total'] = sum(gols)
print('=-' * 30)
print(f' O jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas.')
for v, c in enumerate(gols):
    print(f'     => Na {v +1}ª partida fez {c} gols.')
print(f' Totalizando {jogador["total"]} gols')
print('=-' * 30)
