teste = list()
teste.append('Gustavo')
teste.append(40)
print(teste)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)
galera1 = [['João', 19], ['Ana', 23], ['Joaquim', 13], ['Maria', 45]]
print(galera1[2][1])
for p in galera1:
    print(p[0])
galera2 = list()
dado = list()
for c in range(0,3):
    dado.append(input('Nome: '))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
ma = me =0
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        ma += 1
    else:
        print(f'{p[0]} é menor de idade')
        me += 1
print(f'Temos {ma} maiores e `{me} menores de idade.')