n = int(input('Primeiro termo da PA: '))
r = int(input('Razão da PA: '))
termo = int(input('Quantos termos dessa PA você quer saber? '))
cont = 0
soma = 0
cont = 1
t = 1
print(f'Primeiros {termo} dessa PA são: {n}, ', end='')
while cont < termo and termo != 0:
    n += soma + r
    cont += 1
    t += 1
    print(f'{n}', end=' ')
    print(',' if cont < termo else '', end=' ')
    if termo == cont:
        cont = 0
        print('')
        termo = int(input('Mais quantos termos dessa PA você quer saber? '))
print(f'A progressão foi finalizada com {t} termos mostrados')
print('FIM')