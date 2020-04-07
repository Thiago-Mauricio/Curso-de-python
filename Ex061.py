n = int(input('Primeiro termo da PA: '))
r = int(input('Razão da PA: '))
cont = 0
soma = 0
print(f'Os 10 primeiros termos dessa PA são: {n}, ',end='')
while cont < 9:
    n += soma + r
    cont += 1
    print(f'{n}', end='')
    print(f',' if cont < 9 else'', end=' ')