'''Faça um programa que leia 5 valores numéricos em uma lista.
No final. mostra qual foi o maior e o menor valor digitado e as suas respectivas posições:'''
v = []
ma = me = cont1 = 0
for c in range(0, 5):
    v.append(int(input(f'Digite um valor: ')))
    #pegando o maior e menor direto do input do n, sem precisar colocar na lista
    if c == 0:
        ma = v[c]
        me = v[c]
    else:
        if v[c] > ma:
            ma = v[c]
        if v[c] < me:
            me = v[c]
print(f'Os valores digitados foram {v}')
print(f'O maior valor digitado foi {ma} na posição(s) ', end=' ')
for i, p in enumerate(v):
    if v[i] == ma:
        print(i + 1, end=' ')
print()
print(f'O menor valor Digitado foi {me} na posição(s) ', end=' ')
for t, pm in enumerate(v):
    if v[t] == me:
        print(t + 1, end=' ')
print()
