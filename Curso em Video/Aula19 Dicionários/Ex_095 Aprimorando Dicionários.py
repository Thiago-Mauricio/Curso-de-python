'''Aprimore o Exercicio 093 para que ele funciona com vários jogadores incluindo um sistema de detalhes do aproveitamento de cada jogador'''
jogadores = []
while True:
    jogador = {}
    gols = []
    print('=-' * 30)
    jogador['nome'] = input('Nome do jogador: ').strip().capitalize()
    jogador['partidas'] = int(input('Quantidade de partidas jogadas: '))
    print('=-' * 30)
    for c in range(0, jogador['partidas']):
        gols.append(int(input(f'Gols na {c + 1}ª partida: ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols[:])
    jogadores.append(jogador)
    del gols
    stop = ''
    while stop != 'N' and stop != 'S':
        stop = input('Deseja continuar? [S/N] ').strip().upper()
    if stop == 'N':
        break
print('=-' * 30)
print('{:<3} | {:<20}| {:<20}'.format('COD', 'NOME', 'Total de Gols'))
for i, v in enumerate(jogadores):
    print('{:<3} | {:<20}| {:^14}'.format(i, jogadores[i]["nome"], jogadores[i]["total"]))
print('=-' * 30)
while True:
    cod = int(input('Digite o código do jogador para ver o aproveitamento em partidas: '))
    if cod > len(jogadores) or cod < 0:
        print('Código de jogador inválido.')
        print('=-' * 30)
    else:
        print(f'O jogador {jogadores[cod]["nome"]} fez: ')
        for v, c in enumerate(jogadores[cod]['gols']):
            print(f'     => Na {v +1}ª partida {c} gols.')
        print('=-' * 30)
        print(f' Totalizando {jogadores[cod]["total"]} gols')
    stop = ''
    while stop != 'N' and stop != 'S':
        stop = input('Deseja continuar? [S/N] ').strip().upper()
    if stop == 'N':
        break

    print('=-' * 30)