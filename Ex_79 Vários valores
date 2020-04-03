'''Crie um programa onde o usuário possa digitar vários números e cadastre-os em uma lista. Caso o número já exista dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.'''

n = []
while True:
    print('=' * 40)
    v = int(input('Digite um valor: '))
    if v in n:
        print('Valor duplicado, não vou adicionar.')
    else:
        n.append(v)
    stop = ''
    while stop != 'S' and stop != 'N':
        stop = input('Quer continuar? [S/N] ').strip().upper()
    if stop == 'N':
        break
print('=' * 40)
print(f'Os númeors digitados foram: {sorted(n)}')