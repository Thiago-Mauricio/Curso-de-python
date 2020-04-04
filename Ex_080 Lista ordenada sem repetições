'''Crie um programa onde o usuário possa digitar cinco números e cadastre-os em uma lista, já na posição correta de inserção(sem usar sort()). No final mostre a lista ordenada na tela.'''

n = []
n1 = int(input('Digite um valor: '))
n.append(n1)
print('Valor adicionado a lista!')
print('=' * 50)
n1 = int(input('Digite um valor: '))
if n1 < n[0]:
    n.insert(0, n1)
    print('Adicionado no começo da lista!')
else: 
    n.insert(1, n1)
    print('Adicionado no final da lista!')
print('=' * 50)
n1 = int(input('Digite um valor: '))
if n1 < n[0]:
    n.insert(0, n1)
    print('Adicionado no começo da lista!')
elif n1 > n[0] and n1 <n [1]:
    n.insert(1, n1)
    print('Adicionado na posição 1 da lista!')
else:
    n.append(n1)
    print('Adicionado no final da lista!')
print('=' * 50)
n1 = int(input('Digite um valor: '))
if n1 < n[0]:
    n.insert(0, n1)
    print('Adicionado no começo da lista!')
elif n1 > n[0] and n1 <n [1]:
    n.insert(1, n1)
    print('Adicionado na posição 1 da lista!')
elif n1 > n[1] and n1 < n[2]:
    n.insert(2, n1)
    print('Adicionado na posição 2 da lista!')
else:
    n.append(n1)
    print('Adicionado no final da lista!')
print('=' * 50)
n1 = int(input('Digite um valor: '))
if n1 < n[0]:
    n.insert(0, n1)
    print('Adicionado no começo da lista!')
elif n1 > n[0] and n1 <n [1]:
    n.insert(1, n1)
    print('Adicionado na posição 1 da lista!')
elif n1 > n[1] and n1 < n[2]:
    n.insert(2, n1)
    print('Adicionado na posição 2 da lista!')
elif n1> n[2] and n1 < n[3]:
    n.insert(3, n1)
    print('Adicionado na posição 3 da lista!')
else:
    n.append(n1)
    print('Adicionado no final da lista!')
print('=' * 50)
print(f'Os valores digitados foram {n}.')


#Solução do professor:
lista = []
for c in range(0,5):
    a = int(input('Digite um valor: '))
    if c == 0 or a > lista [-1]:
        lista.append(a)
        print('Adicionado no final da lista!')
    else:
        pos = 0
        while pos < len(lista):
            if a <= lista[pos]:
                lista.insert(pos, a)
                print(f'Adicionado na posição {pos} da lista!')
                break
            pos += 1
print('-' * 40)
print(f'Os valores digitados em ordem foram {lista}')