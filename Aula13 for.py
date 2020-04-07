for c in range(1, 3):
    print('Oi')
print('FIM')

n = int(input('Digite um numero: '))
for h in range(0, n+1):
    print(h)

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for j in range(i, f+1, p):
    print(j)
print('FIM')

s = 0
for c1 in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print(f'O somatório de todos os valores foi {s}')