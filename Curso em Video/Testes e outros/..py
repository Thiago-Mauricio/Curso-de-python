d = list()
pessoas = []
while True:
    d.append(input('Nome: '))
    d.append(float(input('Peso: ')))
    pessoas.append(d[:])
    d.clear()
    stop = ''
    while stop != 'N' and stop != 'S':
        stop = input('Quer continuar? [S/N]')
    if stop == 'N':
        break