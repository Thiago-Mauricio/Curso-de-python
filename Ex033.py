print('Digite três números inteiros!')
#modelo do professor: (mais simples)
a = int(input('Primeiro número: '))
b = int(input('Segundo número: '))
c = int(input('Terceiro número: '))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f'O menor numero é {menor} e o maior é {maior}')
print('=====FIM=====')

#Meu primeiro modelo:
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))
if n1>  n2 and n1 > n3:
    print(f'{n1} é o maior numero e;')
if n2 > n1 and n2 > n3:
    print(f'{n2} é o maior número e;')
if n3 > n1 and n3 > n2:
    print(f'{n3} é o maior número e;')
if n1 < n2 and n1 < n3:
    print(f'{n1} é o menor número!')
if n2 < n1 and n2 < n3:
    print(f'{n2} é o menor número!')
if n3 < n1 and n3 < n2:
    print(f'{n3} é o menor número!')
print('=====FIM=====')
