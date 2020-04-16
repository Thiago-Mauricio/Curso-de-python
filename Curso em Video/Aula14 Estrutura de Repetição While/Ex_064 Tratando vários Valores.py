#método que usei:
n = 0
s = 0
c = 0
p = ''
while n != 999:
    n = int(input('Digite números inteiros para somar, e digite 999 para parar o programa: '))
    s += n
    p += ' ' + str(n).replace('999','')
    c += 1
print(f'Os numeros digitados foram: {p}')
print(f'Você digitou {c-1} números e a soma entre eles foi: {s - 999}')

#método do professor
cont = soma = 0
num = int(input('Digite um número [999 para parar]: '))
while num != 999:
    soma += num
    cont + 1
    num = int(input('Digite um número [999 para parar]: '))
print(f'você digitou {cont} números e a soma entre eles foi {soma}.')