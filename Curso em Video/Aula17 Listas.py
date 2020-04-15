l = []
for c in range(1,10):
    l.insert(0, c)
print(l)
l = []
for c in range(1,10):
    l.append(c)
print(l)

num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 0)
if 4 in num:
    num.remove(4)
print(num)
print(f'essa lista tem {len(num)} elementos.')

valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for v in valores:
    print(f'{v}...', end='')
print('')
for c, i in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {i}!')
print('Cheguei ao final da lista !')

a = [2, 3, 4, 7]
#ligação entra a listas b = a, a = b
b = a
#cópia da lista:
c = a[:]
b[2] = 8

print(f'Lista: {a}')
print(f'Lista: {b}')
print(f'Lista: {c}')