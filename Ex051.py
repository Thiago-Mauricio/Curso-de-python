print('=' * 100)
print('10 TERMOS DE UMA PA: ')
print('=' * 100)
n = int(input('Primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
f = n + (r * 10)
for pa in range(n, f, r):
    print(pa, end=' ')
print('FIM !!!')

