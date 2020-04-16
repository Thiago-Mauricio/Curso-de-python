from random import randint
v = 0
print('=-' * 50)
print('VAMOS JOGAR PAR OU ÍMPAR !!!')
print('=-' * 50)
while True:
    j = input('Par ou Ímpar ? [P/I]: ').strip().upper()[0]
    while j != 'P' and j != 'I':
        j = input('Comando inválido: DIGITE [P] OU [I]: ').strip().upper()[0]
    print('-' * 100)
    n = int(input('Agora digite um valor: '))
    c = randint(0, 10)
    s = n + c
    print(f'Você jogou {n} e o computador {c}. Total deu {s}','Par' if s % 2 == 0 else 'Ímpar')
    #condições de vitória do jogador
    if j == 'P' and s % 2 == 0 or j == 'I' and s % 2 != 0:
        print('=-' * 50)
        print('Parabêns você Ganhou. Vamos jogar de novo!!!')
        v += 1
    #condições de derrota do jogador
    elif j == 'P' and s % 2 !=0 or j == 'I' and s % 2 == 0:
        print('=-' * 50)
        print('Você Perdeu !!!')
        break
print('=-' * 50)
print(f'Você ganhor {v} vezes.')
print('FOI UM BOM JOGO !!!')