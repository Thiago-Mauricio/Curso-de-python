'''Aprimore o exercicio antrios, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
c) O maior valor da segunda linha'''
matriz = [[], [], []]
for c in range(0,3):
    matriz[0].append(int(input(f'Digite um valor para posição [0, {c}]: ')))
for c in range(0,3):
    matriz[1].append(int(input(f'Digite um valor para posição [1, {c}]: ')))
for c in range(0, 3):
    matriz[2].append(int(input(f'Digite um valor para posição [2, {c}]: ')))
print('=' * 40)
sp = 0
for c in matriz[0]:
    print(f'[{c:^5}]', end='')
    if c % 2 == 0:
        sp += c
print()
for c in matriz[1]:
    print(f'[{c:^5}]', end='')
    if c % 2 == 0:
        sp += c
print()
for c in matriz[2]:
    print(f'[{c:^5}]', end='')
    if c % 2 == 0:
        sp += c
print()
print('=' * 40)
print(f'A soma de todos os números pares da matriz é {sp}')
print(f'A soma de todos os números da terceira coluna é {matriz[0][2] + matriz[1][2] + matriz[2][2]}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')