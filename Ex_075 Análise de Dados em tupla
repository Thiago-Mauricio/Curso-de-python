'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final mostre:

A) Quantas vezes apareceu o número 9.
B) Em que posição foi digitado o primeiro valor 3.
C)Quais foram os números Pares'''

a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
c = int(input('Digite outro número: '))
d = int(input('Digite outro número: '))
t = (a, b, c, d)
print(f'Você digitou os valores{t}')
print(f'O valor 9 apareceu {t.count(9)} vezes')
if 3 in t:
    print(f'O valor 3 apareceu pela primeira vez na posição {t.index(3) + 1}')
else:
    print('O número 3 não apareceu!')
print(f'Os valors pares digitados foram: ', end='')
for p in t:
    if p % 2 == 0 and p != 0:
        print(p, end=' ')