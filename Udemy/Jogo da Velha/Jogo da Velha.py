print('=-' *30)
print('{:^55}'.format('JOGO DA VELHA PYTHON'))
print('=-' *30)




while True:
    print('')
    print('')
    print(.format('[1] JOGAR'))
    print('')
    print('')
    print(.format('[2] SAIR'))
    print('')
    print('')
    stop = ''
    while stop != '1' and stop != '2':
        stop = input('Digite sua opção:[1/2] ')
    if stop == '2':
        break
    else:
        while True:
