from math import factorial
n = int(input('Digite um número para saber seu fatorial: '))
#usando o modulo é possivel fazer direto, sem precisar usar while ou for
f = factorial(n)
soma = n
cont = n-1
print(f'Calculando {n}! = {n} X ', end='')
while cont != 0:
    print(f'{cont} ', end='')
    print('X' if cont > 1 else ' = ', end=' ')
    soma = soma * cont
    cont -= 1
print(f'O fatorial de {n} é {soma}')

som1 = n
cont1 = n-1
for c in range(1, n, -1):
    soma1 = soma1 * cont1
    cont1 - 1
print(soma)
print(f)