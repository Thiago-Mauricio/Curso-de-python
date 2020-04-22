from time import sleep
def tabuleiro():
    """
    Cria o tabuleiro do jogo a partir de uma lista com 4 listas internas.
    """ 
    print('-=' * 30)
    print('{:20}'.format(' '), end='')
    # imprime os numerais das colunas na parte superior do tabuleiro
    for c in field[0]:
        print(f'{c:^4}', end ='')
    print()    
    cont = 0
    print('{:20}'.format(' '), end='')
    # imprime a primeira linha do tabuleiro
    for c in field[1]:
        cont += 1
        print(f'{c:^3}', end='')
        print('|' if 1 < cont < 4 else '', end='')
    print()
    cont = 0
    print('{:20}'.format(' '), end='')
    #imprime a segunda linha do tabuleiro
    for c in field[2]:
        cont += 1
        print(f'{c:^3}', end='')
        print('|' if 1 < cont < 4 else '', end='')
    print()
    cont = 0
    print('{:20}'.format(' '), end='')
    # imprime a terceira linha do tabuleiro
    for c in field[3]:
        cont += 1
        print(f'{c:^3}', end='')
        print('|' if 1 < cont < 4 else '', end='')
    print()
    print('-=' * 30)

def jogada(linha, coluna, jogada):
    """
    Função que aaplica a jogada no tabuleiro, usada internamente na função jogador.
    """
    field[linha][coluna] = jogada

def jogador1():
    """
    Recebe a jogada pro primeiro jogador, representado pelo "X"
    """
    print(f'É A VEZ DO JOGADOR 1 "X"')
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
    """
    Recebe a jogada do segundo jogador, reprentado pelo "O"
    """
    print(f'É A VEZ DO JOGADOR 2 "O"')
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
    """
    Aplica as regras de vitória ou empate e caso um dos dois aconteça retorna o resultado, uma cópia do tabuleiro e a interrupção do while
    """
    global continua
    cont = 0
    # conta a quantidades de X e O no tabuleiro para verificação de empate
    for c in field:
        for v in c:
            if 'X' in v or 'O' in v:
                cont += 1
    #confere se algum jogador completou alguma linha, e caso tenha completado retorna o jogador e o resultado
    if field[1] == ['1', '_X_', '_X_', '_X_'] or field [1] == ['1', '_O_', '_O_', '_O_'] or field[2] == ['2', '_X_', '_X_', '_X_'] or field[2] == ['2', '_O_', '_O_', '_O_'] or field[3] == ['3', 'X', 'X', 'X'] or field [3] == ['3', 'O', 'O', 'O']:
        tabuleiro()
        print(f'{jogador} VENCEU !')
        print('-=' * 30)
        sleep(3)
        continua = 1
        return continua
    #confere se algum jogador completou alguma coluna ou diagonal, e caso tenha completado retorna o jogador e o resultado
    elif field[1][1] == '_X_' and field [2][1] == '_X_' and field[3][1] == 'X' or field[1][2] == '_X_' and field [2][2] == '_X_' and field[3][2] == 'X' or field[1][3] == '_X_' and field [2][3] == '_X_' and field[3][3] == 'X' or field[1][1] == '_X_' and  field [2][2] == '_X_' and field[3][3] == 'X' or field[3][1] == 'X' and field [2][2] == '_X_' and field[1][3] == '_X_' or field[1][1] == '_O_' and field [2][1] == '_O_' and  field[3][1] == 'O'  or field[1][2] == '_O_' and  field [2][2] == '_O_' and field[3][2] == 'O'  or field[1][3] == '_O_' and field [2][3] == '_O_' and field[3][3] == 'O'  or field[1][1] == '_O_' and field [2][2] == '_O_' and field[3][3] == 'O'  or field[3][1] == 'O' and field [2][2] == '_O_' and field[1][3] == '_O_':
        tabuleiro()
        print(f'{jogador} VENCEU !')
        print('-=' * 30)
        sleep(3)
        continua = 1
        return continua
    # confere se o tabuleiro esta completo usando a contagem de "X" e "O"
    elif cont == 9:
        tabuleiro()
        print('Empatou')
        print('-=' * 30)
        sleep(3)
        continua = 1
        return continua
    

def menu():
    """
    Imprime o menu do jogo
    """
    print('=' * 60)
    print('{:^57}'.format('MENU'))
    print('-=' * 30)
    print('''
                        JOGAR:  [1]

                        SAIR:   [2]
    ''')
    print('-=' * 30)  


print('=-' *30)
print('{:^55}'.format('JOGO DA VELHA PYTHON'))
print('=-' *30)
#while do menu
while True:
    #lista do tabuleiro, limpa o tabuleiro antigo em caso de novo jogo
    field = [['0', '1', '2', '3'], ['1', '___', '___', '___'], ['2', '___', '___', '___'], ['3', '', '', '']] 
    # variavel para break do jogo
    continua = 0
    #imprime menu
    menu()
    stop =''
    #Se o jogador ecolher jogar o jogo é iniciado, caso escolha sair o jogo é fechado
    while stop != '1' and stop != '2':
        stop = input('           Digite [1] para JOGAR e [2] para SAIR: ').strip()
    print('=' * 60) 
    if stop == '2':
        break
    #whlie do jogo
    while True:
        #imprime o tabuleiro
        tabuleiro()
        #recebe a primeira jogada
        jogador1()
        jogador = 'JOGADOR 1'
        #checa se alguma condição de break foi alcançada
        fim()
        if continua > 0:
            break
        #atualiza o tabuleiro
        tabuleiro()
        #recebe a segunda jogada
        jogador2()
        jogador = 'JOGADOR 2'
        #checa novamente condição de break foi alcançada
        fim()
        if continua > 0:
            break
        
print('-' * 25, ' FIM ', '-' * 28)