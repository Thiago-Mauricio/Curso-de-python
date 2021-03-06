'''Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) Média de idade do grupo
C) Uma lista com todas as mulheres
D) Uma lista com todas as pessoas com idade acima da média'''
cadastro = []
soma = 0
while True:
    pessoa = {}
    pessoa['nome'] = input('Nome: ')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    pessoa['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()
    while pessoa['sexo'] != 'M' and pessoa['sexo'] != 'F':
        pessoa['sexo'] = str(input('Sexo Inválido. Digite [M/F]: ')).strip().upper()
    cadastro.append(pessoa)
    stop = ''
    while stop != 'S' and stop != 'N':
        stop = input('Deseja continuar? [S/N] ').strip().upper()
    if stop == 'N':
        break
média = soma / len(cadastro)
print('=-' * 30)
print(f'Foram cadastradas {len(cadastro)} pessoas no total.')
print('=-' * 30)
print(f'A idade média do grupo é de {média:.1f} anos')
print('=-' * 30)
print('As mulheres cadastradas foram: ', end=' ')
for c in range(0, len(cadastro)):
    if cadastro[c]['sexo'] == 'F':
        print(cadastro[c]['nome'], end=' ')
print()
print('=-' * 30)
print('As pessoas cadatradas com idade superio a média do grupo foram: ', end='')
for c in range(0, len(cadastro)):
    if cadastro[c]['idade'] > média:
        print(cadastro[c]['nome'], end=' ')
print()
print('=-' * 30)