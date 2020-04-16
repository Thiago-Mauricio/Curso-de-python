
c = 1
while c < 3:
    print(c)
    c +=1
print('FIM')
n = 1
while n!= 0:
    n = int(input('Digite um valor: '))
print('FIM')
r = 'S'
while r == 'S':
    n1 = int(input('Digite um valor: '))
    r = input('Quer continuar [S/N] ?  ').upper().strip()
n2 = 1
par = 0
impar = 0
ppar = ''
pimpar = ''
while n2 != 0:
    n2 = int(input('Digite um valor: '))
    if n2 != 0:
        if n2 % 2 == 0 and n2 != 0:
            par += 1
            ppar += str(n2).replace('', ' ')
        else:
            impar += 1
            pimpar += str(n2).replace('', ' ')
print(f'Par: {par}, Impar: {impar}.')
print(f'{ppar}, {pimpar}')