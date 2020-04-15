s = 0
cont = 0
print('Digite a seguir 6 números inteiro:')
for c in range(1,7):
    n = int(input(f'{c}º número: '))
    if n % 2 == 0 and n != 0:
       #s += n é uma simplificação de s = s + n
        s += n
        cont += 1
print(f'Você informou {cont} numeros pares e a soma entre eles foi de {s}.')