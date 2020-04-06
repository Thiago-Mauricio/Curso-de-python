'''Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final mostre
A) Quantas Pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas
C) Uma listagem com as pessoas mais leves'''

dados = []
pessoas = []
while True:
    dados.append(input('Nome: '))
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    stop = ''
    while stop != 'N' and stop != 'S':
        stop = input('Deseja continuar? [S/N] ').strip().upper()
    if stop == 'N':
        break
maior = []
menor = []
acima = []
abaixo = []
for c in pessoas:
    if c == pessoas[0]:
        maior = c
        menor = c
    else:
        if c[1] >= maior[1]:
            maior = c
        if c[1] <= menor[1]:
            menor = c
    if c[1] >= 100:
        acima.append(c[0])
    if c[1] <= 70:
        abaixo.append(c[0])
print(f'Foram cadastradas {len(pessoas)} pessoas')
print(f'A pessoa mais pesada cadastrada foi {maior[0]} com {maior[1]}Kg')
print(f'A pessoa mais leve cadastrada foi {menor[0]}, com {menor[1]}Kg')
print(f'As pessoas acima de 100 kg foram {acima}')
print(f'As pessoas com menos de 70 Kg foram {abaixo}')