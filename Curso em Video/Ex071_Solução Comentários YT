saque = int(input('Sacar R$: '))
cedulas = [1, 10, 20, 50]
c = 3
while saque > 0:
    qtdced = saque // cedulas[c]
    saque -= qtdced * cedulas[c]
    if qtdced > 0:
        print(f'{qtdced} cédulas de R$ {cedulas[c]}')
    c -= 1