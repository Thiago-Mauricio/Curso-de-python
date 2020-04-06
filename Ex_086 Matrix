'''Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final mostra a matriz na tela com formatação correta'''


l1 = []
l2 = []
l3 = []
for a in range(0, 3):
    l1.append(int(input(f'Digite um número para posição 1, {a}: ')))
for b in range(0, 3):
    l2.append(int(input(f'Digite um número para posição 2, {b}: ')))
for c in range(0, 3):
    l3.append(int(input(f'Digite um número para posição 3, {c}: ')))
print('-' * 40)
print('|', end=' ')
for d in l1:
    print(f'{d:^5}', end='')
print('|')
print('|', end=' ')
for e in l2:
    print(f'{e:^5}', end='')
print('|')
print('|', end=' ')
for f in l3:
    print(f'{f:^5}', end='')
print('|')

#modelo professor:
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for co in range(0, 3):
        matriz[l][co] = int(input(f'Digite um valor para [{l}], {co}: '))
print('-=' * 30)
for l in range(0, 3):
    for co in range(0, 3):
        print(f'[{matriz[l][co]:^5}]', end=' ')
    print()