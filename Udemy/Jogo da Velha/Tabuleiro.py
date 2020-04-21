from time import sleep
field = [['0', '1', '2', '3'], ['1', '___', '___', '___'], ['2', '___', '___', '___'], ['3', '', '', '']] 
def tabuleiro(): 
    print('-=' * 30)
    print('{:20}'.format(' '), end='')
    for c in field[0]:
        print(f'{c:^4}', end ='')
    print()    
    cont = 0
    print('{:20}'.format(' '), end='')
    for c in field[1]:
        cont += 1
        print(f'{c:^3}', end='')
        print('|' if 1 < cont < 4 else '', end='')
    print()
    cont = 0
    print('{:20}'.format(' '), end='')
    for c in field[2]:
        cont += 1
        print(f'{c:^3}', end='')
        print('|' if 1 < cont < 4 else '', end='')
    print()
    cont = 0
    print('{:20}'.format(' '), end='')
    for c in field[3]:
        cont += 1
        print(f'{c:^3}', end='')
        print('|' if 1 < cont < 4 else '', end='')
    print()
    print('-=' * 30)

def jogada(linha, coluna, jogada):
    field[linha][coluna] = jogada

def jogador1():
    print(f'É A VEZ DE')
    while True:
        while True:
            try:
                linha = int(input('Digite o número da linha da sua jogada: '))
                coluna = int(input('Digite o número da coluna da sua jogada: '))
                break
            except:
                print('Erro: Digite apenas números!')
        if linha < 1 or linha > 3 or coluna < 1 or coluna > 3:
            print('Erro: O valor de coluna e linha devem ser entre 1 e 3!')
        else:
            break
    while field[linha][coluna] == '_X_' or field[linha][coluna] == '_O_':
        print('Célula já prenchida: Digit outro valor')
        linha = int(input('Digite o número da linha da sua jogada: '))
        coluna = int(input('Digite o número da coluna da sua jogada: '))    
    if linha == 3:
        return jogada(linha, coluna, 'X')
    else:
        return jogada(linha, coluna, '_X_')

def jogador2():
    print(f'É A VEZ DE')
    while True:
        while True:
            try:
                linha = int(input('Digite o número da linha da sua jogada: '))
                coluna = int(input('Digite o número da coluna da sua jogada: '))
                break
            except:
                print('Erro: Digite apenas números!')
        if linha < 1 or linha > 3 or coluna < 1 or coluna > 3:
            print('Erro: O valor de coluna e linha devem ser entre 1 e 3!')
        else:
            break
    while field[linha][coluna] == '_X_' or field[linha][coluna] == '_O_':
        print('Célula já prenchida: Digit outro valor')
        linha = int(input('Digite o número da linha da sua jogada: '))
        coluna = int(input('Digite o número da coluna da sua jogada: '))    
    if linha == 3:
        return jogada(linha, coluna, 'O')
    else:
        return jogada(linha, coluna, '_O_')
    
def fim():
    contiua = True
    if field[1] == ['1', '_X_', '_X_', '_X_'] or field [1] == ['1', '_O_', '_O_', '_O_'] or field[2] == ['2', '_X_', '_X_', '_X_'] or field[2] == ['2', '_O_', '_O_', '_O_'] or field[1] == ['1', '_X_', '_X_', '_X_'] or field [1] == ['1', '_O_', '_O_', '_O_']:
        print('-=' * 30)
        print(f'Venceu !')
        print('-=' * 30)
        sleep(3)
        return contiua == False
    elif field[1][1] == field [2][1] == field[3][1] or field[1][2] == field [2][2] == field[3][2] or field[1][3] == field [2][3] == field[3][3] or field[1][1] == field [2][2] == field[3][3] or field[3][1] == field [2][2] == field[1][3]:
        print('-=' * 30)
        print('Venceu !')
        print('-=' * 30)
        sleep(3)
        return contiua == False
    cont = 0
    for c in field:
        for v in c:
            if 'X' in v or 'O' in v:
                cont += 1
    if cont == 9:
        print('-=' * 30)
        print('Empatou')
        print('-=' * 30)
        sleep(3)
        return contiua == False

continua = True
while continua:
    tabuleiro()
    jogador1()
    fim()
    tabuleiro()
    jogador2()
    fim()