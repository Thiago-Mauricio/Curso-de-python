from random import randint
print(randint(10, 121))

lista = (
    'Lápis', 1.50,
    'borracha', 2.00,
    'caderno', 15.0,
    'estojo', 9.00,
    'caneta', 2.50,
    'apontador', 1.00
)
print('-' * 40)
for c in range(0, len(lista)):
    if c % 2 == 0:
        print('{:.<30}'.format(lista[c]), end='')
    else:
        print('R$ {:>4.2f}'.format(lista[c]))
print('-' * 40)
