n = int(input('Quantos termos da sequência fibonacci você quer mostrar ? '))
s = 0
c = 3
t1 = 0
t2 = 1
print(f' {t1} -> {t2}', end=' -> ')
while n >= c:
    t3 = t1 + t2
    c += 1
    print(f'{t3}', end=' -> ')
    t1 = t2
    t2 = t3
print('FIM')