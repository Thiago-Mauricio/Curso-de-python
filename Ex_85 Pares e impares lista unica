'''Crie um programa onde o usuário possa digitar sete valores numéricos e cadastreos em uma lista única, que mantenha separados os valores pares e impares. No final, mostre os valores pares e ímpares em ordem crescente'''
num = []
par = []
impar = []
for c in range(1, 8):
    n = int(input('Digite um valor: '))
    if n % 2 == 0 and n != 0:
        par.append(n)
    else:
        impar.append(n)
    num.append(par[:])
    num.append(impar[:])
print(f'Os valores pares digitados foram: {sorted(par)}')
print(f'Os valores ímpares digitados foram: {sorted(impar)}')

#modelo do professor:
núm = [[], []]
for c in range(1,8):
    valor = int(input(f'Digite o {c}o. valor: '))
    if valor % 2 == 0:
        núm[0].append(valor)
    else:
        núm[1].append(valor)
print('-=' * 30)
núm[0].sort()
núm[1].sort()
print(f'Os valores pares digitados foram: {núm[0]}')
print(f'Os valores ímpares digitados foram: {núm[1]}')