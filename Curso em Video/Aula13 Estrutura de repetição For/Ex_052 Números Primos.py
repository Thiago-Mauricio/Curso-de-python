n = int(input('Digite um número inteiro para descobrir se ele é um numero primo: '))
d = 0
print(f'{n} é divisível por:')
for c in range(1, n + 1,):
    if n % c == 0:
        d +=1
        print(c, end=' ')
print('')
if d > 2:
    print(f'E por isso {n} não é um número primo!')
else:
    print(f'E por isso {n} é um número primo')
