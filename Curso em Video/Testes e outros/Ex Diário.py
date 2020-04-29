from random import randint
print(randint(10, 121))

while True:
    while True:    
        try:
            n1 = int(input('Digite um valor: '))
            n2 = int(input('Digite outro valor: '))
            break
        except:
            print('Erro: Ambos os valores precisam ser números inteiros:')
    if n1 > n2:
        print(f'{n1} é maior que {n2} !')
    elif n1 == n2:
        print (f'{n1} e {n2} são iguais!')
    else:
        print(f'{n2} é maior que {n1} !')
    stop = ''
    while stop != 'N' and stop != 'S':
        stop = input('Deseja continuar? [S/N] ').strip().upper()
    if stop == 'N':
        break
print('FIM !')