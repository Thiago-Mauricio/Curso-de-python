ma = me = s = c = 0
while True:
    n = int(input('Dígite um número: '))
    c += 1
    s += n
    if c == 1 :
        ma = n
        me = n
    else:
        if n > ma:
            ma = n
        if n < me:
            me = n
    f = input('Quer continuar? [S/N]: ').strip().upper()[0]
    while f != 'N' and f != 'S':
        f = input('Comando inválido: digite S para continuar ou N para parar: ').strip().upper()[0]
    if f == 'N':
        break
m = s / c
print(f'Você digitou {c} numéros, a média entre eles foi de: {m}, sendo {ma} o maior e {me} o menor.')