from random import choice
from unidecode import unidecode
from time import sleep
print('\033[1;31;40m-=\033[m'*100)
nome = input('QUAL O SEU NOME? ').strip().upper()
print('\033[1;31;40m-=\033[m'*100)
print(f'\033[1;31M                                        {nome}. VAMOS JOGAR JOKENPÔ ???\033[m')
sleep(1)
print('\033[1;31;40m-=\033[m'*100)
#atribuição de resultados pra sorteio do computador:
P = 'PEDRA'
T = 'TESOURA'
PA = 'PAPEL'
while True:
    #comando choice para computador sortear:
    list = [P, T, PA]
    c = choice(list)
    #resultados possiveis para serem adicionados nas condições
    r1 = 'PARABÉNS!!! VOCÊ GANHOU!!!'
    r2 = 'EMPATOU!'
    r3 = 'VOCÊ PERDEU!!!'
    #escolha do jogador
    jogador = input('ESCOLHA: PEDRA, PAPEL OU TESOURA: ').strip().upper()
    while jogador != 'PEDRA' and jogador != 'PAPEL' and jogador != 'TESOURA':
        jogador = input('Jogada inválida: ESCOLHA: PEDRA, PAPEL OU TESOURA: ').strip().upper()
    #tirando acento e colocando a escolha do jogador em maiuscula:
    j = unidecode(jogador.upper())
    #condições para vitória do jogador:
    if j == 'PEDRA' and c == T or j == 'PAPEL' and c == P or j == 'TESOURA' and c == PA:
        r = r1
    #condições de empate:
    elif j == 'TESOURA' and c == T or j == 'PEDRA' and c == P or j == 'PAPEL' and c == PA:
        r = r2
    #condições de vitória do computador:
    elif j == 'PAPEL' and c == T or j == 'PEDRA' and c == PA or j == 'TESOURA' and c == P:
        r = r3
    print(' ' * 50, 'JO...')
    sleep(1)
    print(' ' * 50, 'KEN...')
    sleep(1)
    print(' ' * 50, 'PÔ...')
    sleep(1)
    print(' ' * 50, f'{nome} ({j}) x ({c}) COMPUTADOR.')
    print(' ' * 50, r)
    stop = input('Quer jogar de novo ? [S/N] ').strip().upper()
    while stop != 'S' and stop != 'N':
        stop = input('Quer jogar de novo ? [S/N] ').strip().upper()
    if stop == 'N':
        break
print('\033[1;31;40m-=\033[m' * 100)
