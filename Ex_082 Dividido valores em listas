'''Crie um programa que vai ler vários números e colocar em uma lista.
   Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores impares digitados, respequitivamente.
   Ao final, mostra o conteúdo das três listas geradas.'''

n = []
par = []
impar = []
while True:
    n.append(int(input('Digite um valor: ')))
    stop = ''
    while stop != 'N' and stop != 'S':
        stop = input('Deseja continuar? [S/N] ').strip().upper()[0]
    if stop == 'N':
        break
for a in n:
    if a % 2 == 0:
        par.append(a)
    else:
        impar.append(a)
print(f'Os números digitados foram: {n}')
print(f'Entre os números digitados os pares são: {par}')
print(f'E os impares são {impar}')